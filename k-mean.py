import random as r
import math

class flower :

    def __init__(self,a):
        self.prop=a
        self.group=0

    def get_properties(self):
        return self.prop

    def set_group(self,n):
        self.group=n

    def get_group(self):
        return self.group

class groups :

    def __init__(self,n,p):
        self.grp_no=n
        self.number=p
        self.flower_prop=[0]*p
        self.count=0
        self.flowers=[]

    def add_to_grp(self,a):
        self.flower_prop=[x+y for x,y in zip(self.flower_prop,a)]
        self.count+=1

    def return_avg(self):
        self.flower_prop=[i/self.count for i in self.flower_prop]
        return self.flower_prop

    def update(self):
        self.flower_prop=[0]*self.number
        self.count=0
        self.flowers=[]

    def add_flower(self,n):
        self.flowers.append(n)

    def return_flowers(self) :
        return self.flowers

def distance(a,b):
    dist=0
    for i in range(len(a)):
        dist+=(a[i]-b[i])**2
    return math.sqrt(dist)

def update_grp():
    global grp
    for i in grp :
        grp[i].update()

def update_centres():
    global centres,grp
    for i in centres:
        centres[i]=grp[i].return_avg()

flowers={}
centres={}
grp={}

n=int(input("Enter no.of flowers: "))
g=int(input("No.of groups you wish to do: "))
p=int(input("Enter no.of properties of flowers: "))
print("Enter properties of flowers: ")

for i in range(1,n+1):
    a=input().split(',')
    a=list(map(float,a))
    flowers[i]=flower(a)

for i in range(1,g+1):
    grp[i]=groups(i,p)

for i in range(1,g+1):
    centres[i]=flowers[r.randint(1,n)].get_properties()

it=0
while True:
    count=0
    it+=1
    update_grp()
    for i in flowers:
        a=flowers[i].get_properties()
        fin=2**64
        pos=1
        for j in centres:
            temp=distance(a,centres[j])
            if temp<fin:
                pos=j
                fin=temp
        if pos!=flowers[i].get_group():
            count+=1
            flowers[i].set_group(pos)
        grp[pos].add_to_grp(flowers[i].get_properties())
        grp[pos].add_flower(i)
    if count==0 :
        break
    update_centres()

for i in grp:
    print(grp[i].return_flowers(),len(grp[i].return_flowers()))
