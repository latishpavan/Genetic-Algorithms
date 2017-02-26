import random as r
import math as m

class vector:
    
    def __init__(self,a,b=None):
        self.parent=a
        self.mutant=b
        self.child=None

    def set_mutant(self,b):
        self.mutant=b

    def set_child(self,a):
        self.child=a

    def reset_parent(self,a):
        self.parent=a    
    
    def reset(self):
        self.child=None
        self.mutant=None
    

def gen_random(a):
    global p
    r1,r2,r3=[int(p*0.1*(r.randint(1,10))),int(p*0.1*(r.randint(1,10))),int(p*0.1*(r.randint(1,10)))]
    if r1==r2 or r2==r3 or r1==r3 or r1==a or r2==a or r3==a:
        return gen_random(a)
    else:
        return [r1,r2,r3]

def mutate():
    global vectors,p
    count=0
    while True:
        i=r.randint(1,p)
        if count==p:
            break
        if vectors[i].mutant!=None :
            continue
        r1,r2,r3=gen_random(i)
        f=0.1*(r.randint(0,20))
        mut=[f*(x-y) for x,y in zip(vectors[r2].parent,vectors[r3].parent)]
        mut=[x+y for x,y in zip(mut,vectors[r1].parent)]
        vectors[i].set_mutant(mut)
        count+=1

def recombine():
    global vectors
    for i in vectors :
        child=[]
        if vectors[i].mutant!=None:
            for j in range(2):
                cr=0.1*(r.randint(0,10))
                u=0.1*(r.randint(0,10))
                if u<=cr:
                    child.append(vectors[i].mutant[j])
                else:
                    child.append(vectors[i].parent[j])
            vectors[i].set_child(child)

def calculate(a):
        return m.exp(-a[0])+m.sin(a[1])

def best():
    global vectors
    fin=calculate(vectors[1].parent)
    ind=1
    for i in vectors:
        temp=calculate(vectors[i].parent)
        if temp>fin:
            fin=temp
            ind=i
    return fin,ind

def select():
    global vectors
    for i in vectors:
        vectors[i].mutant=None
        if vectors[i].child!=None:
            v1,v2=[calculate(vectors[i].parent),calculate(vectors[i].child)]
            if v2>v1:
                vectors[i].parent=vectors[i].child
            vectors[i].child=None
            
def verify():
    global vectors,x1,x2,x1_d,x2_d
    for i in vectors:
        temp=vectors[i].parent
        if (temp[0]<x1 or temp[0]>x2) or (temp[1]<x1_d or temp[1]>x2_d):
            vectors[i].parent=[r.randint(x1,x2),r.randint(x1_d,x2_d)]
        
vectors={}
x1=int(input("Please enter left extreme of the interval for x1: "))
x2=int(input("Please enter right extreme of the interval for x1: "))
x1_d=int(input("Please enter left extreme of the interval for x2: "))
x2_d=int(input("Please enter right extreme of the interval for x2: "))
p=int(input("Enter population size: "))

for i in range(1,p+1):
    vectors[i]=vector([r.randint(x1,x2),r.randint(x1_d,x2_d)])

it=0 
while True:
    count=0
    it+=1
    mutate()
    recombine()
    select()
    verify()
    fin,ind=best()
    for i in vectors:
        t=calculate(vectors[i].parent)
        if abs(t-fin)<=0.10:
            count+=1
    if count==p or it>1000:
        break
print(fin,vectors[ind].parent)

    
    
    
