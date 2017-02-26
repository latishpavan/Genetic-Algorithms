import math as m
import random as r


def evaluate(a):
    return m.sin(a[0])+m.cos(a[1])

class swarm:
    def __init__(self,a):
        self.pop=a
        self.vel=[r.uniform(l1,r1),r.uniform(l2,r2)]

    def perform_cso(self):
        global l1,r1,l2,r2
        for i in range(5):
            new_swarm=[r.uniform(l1,r1),r.uniform(l2,r2)]
            if evaluate(new_swarm)>evaluate(self.pop):
                self.pop=new_swarm

    def perform_pso(self,gbest):
        ra=r.uniform(0,1)
        new_pos=[2*ra*(i-j) for i,j in zip(gbest,self.pop)]
        self.vel=[i+j for i,j in zip(self.vel,new_pos)]

    def get_pop(self):
        return self.pop

def get_gbest(pop,list_pso):
    gbest_val=-1000000
    gbest=0
    for i in list_pso:
        if evaluate(pop[i].get_pop())>gbest_val:
            gbest=i
            gbest_val=evaluate(pop[i].get_pop())
    return pop[gbest].get_pop()

def initalise_pop(l1,r1,l2,r2):
    pop={}
    for i in range(50):
        pop[i+1]=swarm([r.uniform(l1,r1),r.uniform(l2,r2)])
    return pop

def get_rand_list():
    pso=[]
    count=0
    while count<10:
        ra=r.randint(1,50)
        if ra in pso:
            continue
        pso.append(ra)
        count+=1
    return pso

def final_ans(population):
    best_val=-10000
    best_ind=0
    for i in population:
        if(evaluate(population[i].get_pop())>best_val):
            best_val=evaluate(population[i].get_pop())
            best_ind=i
    print(best_val,population[best_ind].get_pop())

print("Enter the limits of first variable: ")
l1,r1=input().split(' ')
l1,r1=[float(l1),float(r1)]
print("Enter the limits of second variable: ")
l2,r2=input().split(' ')
l2,r2=[float(l2),float(r2)]
population=initalise_pop(l1,r1,l2,r2)

it=400
while it>0:
    pso_list=get_rand_list()
    for i in population:
        if i not in pso_list:
            population[i].perform_cso()
    gbest=get_gbest(population,pso_list)
    for i in pso_list:
        population[i].perform_pso(gbest)
    it-=1

final_ans(population)
