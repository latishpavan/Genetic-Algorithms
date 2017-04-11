import numpy as np
import operator as op
import math as m
import random as r

f=lambda n:m.sin(n)

def initialise(pop,p,l,r1):
	for i in range(p):
		pop[i+1]=r.uniform(l,r1)

def mutate(b,p):
	best=[b]*p;d=0;n=0.1
	for i in range(int(0.8*p)):
		ran=r.uniform(0,1)
		if ran<=0.5:d=(2*ran**(1/(n+1)))-1
		else:ran=1-(2*(1-ran))**(1/(n+1))
		best[i]=b+d
	return best

def clone_pop(pop,p):
	values=list(pop.values())
	value=[f(i) for i in values]
	sort_index=np.argsort(value)
	best_pop=pop[sort_index[-1]+1]
	best=mutate(best_pop,p)
	values.extend(best)
	fin_values=[f(i) for i in values]
	sorted_ind=np.argsort(fin_values)[::-1]
	for i in range(p):
		pop[i+1]=values[sorted_ind[i]]

p,l,r1=input().split(' ')
p,l,r1=[int(p),float(l),float(r1)]
pop={}
initialise(pop,p,l,r1);i=200
while i>0:
	clone_pop(pop,p)
	i-=1
for i in pop:
	print(f(pop[i]),pop[i])
