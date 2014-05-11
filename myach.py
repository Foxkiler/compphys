from visual import *
from random import randint

def Collidewall(f,wall,obj,Omega):
    n=-norm(wall.pos)
    Ia=2*m*l**2
    Vap1=f.velocity+cross(Omega,obj.pos)
    J=-2.0*dot(Vap1,n)/(1.0/M+mag(cross(obj.pos,n))**2/Ia)
    f.velocity=f.velocity+J*n/M
    print Omega
    Omega=Omega+cross(obj.pos,J*n/Ia)
    return Omega

t =0.00
dt=0.01
g =10.0
g=vector(0,g,0)
kfloor=1.0


scene = display(title='Dumpbell',width=1024, height=580,center=(0,0,0), background=(1,1,1))
wallx,wally,wallz=[],[],[]
L=15.0
#wallx.append(    box(pos=(-0.5*L ,0      ,     0), size=(0.1*L   ,L,L), color=(0,0,10), opacity=0)     )
#wallx.append(    box(pos=( 0.5*L ,0      ,     0), size=(0.1*L   ,L,L), color=(0,0,10), opacity=0)     )
wally.append(    box(pos=(0      ,-0.5*L+3 ,     0), size=(L,0.01*L  ,0.1*L), color=(0,0,10), opacity=1.0)     )
#wally.append(    box(pos=(0      , 0.5*L ,     0), size=(L,0.1*L   ,L), color=(0,0,10), opacity=0)     )
#wallz.append(    box(pos=(0      ,0      ,-0.5*L), size=(L,L,  0), color=(0,0,10), opacity=1.0)     )
#wallz.append(    box(pos=(0      ,0      , 0.5*L), size=(L,L,  0), color=(0,0,10), opacity=0.0)     )

l=2.0
f = frame()
box(frame=f, pos=( -l,0,0), size=0.1*vector(1,1,1),color=color.cyan,material=materials.emissive)
box(frame=f, pos=(l,0,0), size=0.1*vector(1,1,1),color=color.cyan,material=materials.emissive)
#box(frame=f, pos=(0,0,0), length=1,color=color.white,material=materials.emissive)
f.axis = vector(1,-1,0)
f.pos = vector(0,0,0)
f.velocity=vector(0,-1,0)

m=1.0
M=2*m

Omega=vector(0,0,1)
while t<100:
    rate (10)
    f.pos=f.pos+f.velocity*dt           -M*g*dt**2/2
    f.velocity=f.velocity               -M*g*dt
    f.rotate(angle=mag(Omega)*dt, axis=Omega, origin=f.pos)
    
    for obj in f.objects:
        S=f.pos+obj.pos
        print S.y
        if S.y<wally[0].pos.y+0.5*wally[0].size.y:
            Omega=Collidewall(f,wally[0],obj,Omega)
    t=t+dt
