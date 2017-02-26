import random as r
import math as m

def evaluate(a):
    try:
        return m.cos(a[0])+m.sin(a[1])
    except ValueError:
        return -5

class swarm :
    c1=2.0
    gbest=[]
    def __init__(self,p,v):
        self.pos=p
        self.vel=v
        self.pbest=p

    def update_vel(self):
        r1,r2=r.uniform(0,1),r.uniform(0,1)
        w=1.1-(swarm.gbest[0]/self.pbest[0])
        self.vel=[w*i for i in self.vel]
        a=[swarm.c1*r1*(i-j) for i,j in zip(self.pbest,self.pos)]
        b=[swarm.c1*r2*(i-j) for i,j in zip(swarm.gbest,self.pos)]
        self.vel=[i+j for i,j in zip(self.vel,a)]
        self.vel=[i+j for i,j in zip(self.vel,b)]

    def update_pos(self):
        self.pos=[i+j for i,j in zip(self.pos,self.vel)]

    def sel_pbest(self,l1,r1,l2,r2):
        k=evaluate(self.pos)
        if k==-5:
            self.pos=[r.uniform(l1,r1),r.uniform(l2,r2)]
        if evaluate(self.pbest)<k:
            self.pbest=self.pos


def update_gbest(particles,g):
    g=particles[1].pbest
    for i in particles:
        if evaluate(g)<evaluate(particles[i].pbest):
            g=particles[i].pbest
    return g

def check(particles):
    global l1,r1,l2,r2
    for i in particles:
        if particles[i].pos[0]<l1 or particles[i].pos[0]>r1 :
            particles[i].pos[0]=r.uniform(l1,r1)
        if particles[i].pos[1]<l2 or particles[i].pos[1]>r2 :
            particles[i].pos[1]=r.uniform(l2,r2)

def terminate(p):
    count=0
    k=evaluate(swarm.gbest)
    for i in p:
        if abs(evaluate(p[i].pbest)-k)<0.00001:
            count+=1
    if count>=0.8*len(p):
        return 1
    return 0

particles={}
p=int(input("Enter population size: "))
l1,r1=input("Enter range of first variable: ").split(' ')
l1,r1=[float(l1),float(r1)]
l2,r2=input("Enter range of second variable: ").split(' ')
l2,r2=[float(l2),float(r2)]
for i in range(p):
    pos=[r.uniform(l1,r1),r.uniform(l2,r2)]
    vel=[r.uniform(l1,r1),r.uniform(l2,r2)]
    particles[i+1]=swarm(pos,vel)

j=0
swarm.gbest=update_gbest(particles,swarm.gbest)
while True:
    for i in particles:
        particles[i].update_vel()
        particles[i].update_pos()
        particles[i].sel_pbest(l1,r1,l2,r2)
    check(particles)
    swarm.gbest=update_gbest(particles,swarm.gbest)
    if terminate(particles) or j>500:
        break
    j+=1
print(evaluate(swarm.gbest),j,swarm.gbest)
