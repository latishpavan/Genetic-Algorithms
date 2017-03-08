import random as r
import operator as op
import matplotlib.pyplot as plt
import math

p,l,ri,inf=100,-10,10,10**5
f1=lambda n:math.sin(n)
f2=lambda n:math.cos(n)

class point:
    def __init__(self,val=None):
        self.val1=f1(val)
        self.val2=f2(val)
        self.x=val
        self.rank=None
        self.cd=None
        self.selected=None

    def set_val(self,val):
        self.val1=f1(val)
        self.val2=f2(val)

    def set_rank(self,r):
        self.rank=r

    def get_rank(self):
        return self.rank

    def set_cd(self,c):
        self.cd=c

    def get_cd(self):
        return self.cd

    def isdominant(self,l):
        if self.val1<l.val1 and self.val2<l.val2:
            return True
        return False

def generate_random(pop):
    for i in range(p):
        pop[i+1]=point(r.uniform(l,ri))

def get_rank(pop,j):
    rank=0
    for i in range(j-1):
        if pop[i+1].isdominant(pop[j]):
            if pop[i+1].get_rank()>rank:
                rank=pop[i+1].get_rank()
    return rank+1

def rank_pop(pop):
    for i in range(len(pop)):
        if i==0:
            pop[i+1].set_rank(1)
        else:
            pop[i+1].set_rank(get_rank(pop,i+1))

def sort_points(pop,temp):
    a={};t=[]
    for i in temp:
        a[i]=pop[i].val1
    a=sorted(a.items(),key=op.itemgetter(1))
    for i in a:
        t.append(i[0])
    return t

def get_cd(pop,temp,i):
    cd=abs((pop[temp[i+1]].val1-pop[temp[i-1]].val1)/(pop[temp[-1]].val1-pop[temp[0]].val1))
    +abs((pop[temp[i+1]].val2-pop[temp[i-1]].val2)/(pop[temp[0]].val2-pop[temp[-1]].val2))
    return cd

def crowd_dist(pop,rank):
    temp=[]
    for i in pop:
        if pop[i].get_rank()==rank:
            temp.append(i)
    if len(temp)==0:
        return 0
    else:
        temp=sort_points(pop,temp)
        for i in range(len(temp)):
            if i==0 or i==len(temp)-1:
                pop[temp[i]].set_cd(inf)
            else:
                pop[temp[i]].set_cd(get_cd(pop,temp,i))
    crowd_dist(pop,rank+1)

def select(pop):
    selected=[]
    count=0
    while count<0.8*p:
        r1,r2=r.randint(1,p),r.randint(1,p)
        if pop[r1].selected!=None or pop[r2].selected!=None:
            continue
        if pop[r1].get_rank()<pop[r2].get_rank():
            selected.append(r1)
            pop[r1].selected=1
        elif pop[r1].get_rank()==pop[r2].get_rank():
            if pop[r1].get_cd()>pop[r2].get_cd():
                selected.append(r1)
                pop[r1].selected=1
            else:
                selected.append(r2)
                pop[r2].selected=1
        else:
            selected.append(r2)
            pop[r2].selected=1
        count+=1
    return selected

def crossover(pop,selected):
    child={}
    for i in range(0,len(selected),2):
        r1=r.uniform(0,1)
        mu=0.8
        if r1<=0.5:
            b=(2*r1)**(1/(mu+1))
        else:
            b=(0.5*(1-r1))**(1/(1+mu))
        c1=point(0.5*((1+b)*pop[selected[i]].x+(1-b)*pop[selected[i+1]].x))
        c2=point(0.5*((1-b)*pop[selected[i]].x+(1+b)*pop[selected[i+1]].x))
        child[p+i+1]=c1
        child[p+i+2]=c2
    return child

def mutate(child,selected,pop):
    n=0.1
    count=0
    while count<0.1*p:
        r1=r.randint(p+1,1.8*p)
        r2=r.uniform(0,1)
        if r2<=0.5:
            d=(2*r2)**(1/(1+n))
        else:
            d=1-(2*(1-r2))**(1/(1+n))
        child[r1].x=pop[selected[r1-p-1]].x+d
        count+=1

def select_next_gen(pop,child):
    new_pop=dict(pop)
    new_pop.update(child)
    rank_pop(new_pop)
    temp={};count=0
    for i in new_pop:
        temp[i]=new_pop[i].get_rank()
    temp=sorted(temp.items(),key=op.itemgetter(1))
    while count<p:
        pop[count+1]=new_pop[temp[count][0]]
        pop[count+1].selected=None
        count+=1
    return pop

def reset(pop):
    for i in pop:
        if pop[i].x<l or pop[i].x>ri:
            pop[i].x=r.uniform(l,ri)

def plot(pop):
    a=[];b=[]
    for i in pop:
        a.append(pop[i].val1)
        b.append(pop[i].val2)
    plt.plot(b,a,'ro')
    plt.xlabel('f1',fontsize=20)
    plt.ylabel('f2',fontsize=20)
    plt.show()

pop={}
generate_random(pop)
plot(pop)
it=0
while it<100:
    reset(pop)
    rank_pop(pop)
    crowd_dist(pop,1)
    selected=select(pop)
    child=crossover(pop,selected)
    mutate(child,selected,pop)
    pop=select_next_gen(pop,child)
    it+=1
plot(pop)
