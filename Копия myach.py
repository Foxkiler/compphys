from visual import *
from random import randint
scene = display(title='Balls to the Wall',width=1024, height=580,center=(0,0,0), background=(1,1,1))
floor = box (pos=(0,0,0), length=10, height=0.01, width=10, color=color.blue, material=materials.emissive)

wallx,wally,wallz=[],[],[]
L=20.0
wallx.append(    box(pos=(-0.5*L ,0      ,     0), size=(0  ,L,L), color=(0,0,10), opacity=0.1)     )
wallx.append(    box(pos=( 0.5*L ,0      ,     0), size=(0  ,L,L), color=(0,0,10), opacity=0.1)     )
wally.append(    box(pos=(0      ,-0.5*L ,     0), size=(L,0  ,L), color=(0,0,10), opacity=0.1)     )
wally.append(    box(pos=(0      , 0.5*L ,     0), size=(L,0  ,L), color=(0,0,10), opacity=0.1)     )
wallz.append(    box(pos=(0      ,0      ,-0.5*L), size=(L,L,  0), color=(0,0,10), opacity=1.0)     )
wallz.append(    box(pos=(0      ,0      , 0.5*L), size=(L,L,  0), color=(0,0,10), opacity=0.0)     )


ball=[1,1,1]
ball[1] = sphere (pos=(1,5,0), radius=0.3, color=color.red, material=materials.emissive)
ball[2] = sphere (pos=(1,3,0), radius=0.3, color=color.green, material=materials.emissive)
#ball[3] = sphere (pos=(2,4,1), radius=0.3, color=color.orange, material=materials.emissive)
ball[1].velocity = vector(1,1,0)
ball[2].velocity=vector(-1,1,0)
#ball[3].velocity=vector(0,3,-1)

#rod=curve (pos=[ball[2].pos, ball[1].pos], radius=0.05, color=color.black, material=materials.emissive)
L=mag(ball[1].pos-ball[2].pos)

t =0.00
dt=0.01
g =1.00
g=vector(0,g,0)
kfloor=1.0

N=len(ball)
while t<100:
    rate (100)
    for i in range(1,N):
        ball[i].pos = ball[i].pos + ball[i].velocity*dt-g*(dt)**2/2
        
        if ball[i].y < ball[i].radius:
            ball[i].velocity.y = kfloor*abs(ball[i].velocity.y)

    S=ball[2].pos-ball[1].pos
    if abs(mag(S)-L)!=0:
        b=L-mag(S)
        vec=norm(S)
        ball[2].pos=ball[2].pos+b/2*vec
        ball[1].pos=ball[1].pos-b/2*vec
    
   # if ball.y < ball.radius and ball.x<=(floor.length/2+ball.radius) and ball.z<=(floor.length/2+ball.radius):
   #     ball.velocity.y = 0.9*abs(ball.velocity.y)#+0.1*ball.velocity.y
   # if ball2.y < ball2.radius and ball2.x<=(floor.length/2+ball2.radius) and ball2.z<=(floor.length/2+ball2.radius):
   #     ball2.velocity.y = 0.9*abs(ball2.velocity.y)#+0.1*ball2.velocity.y
   # if ball3.y < ball3.radius and ball3.x<=(floor.length/2+ball3.radius) and ball3.z<=(floor.length/2+ball3.radius):
    #    ball3.velocity.y = 0.9*abs(ball3.velocity.y)#+0.1*ball3.velocity.y
    for i in range(1,N):    
        ball[i].velocity = ball[i].velocity - g*dt

    t=t+dt
