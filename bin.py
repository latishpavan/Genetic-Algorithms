import random as r
import math as m
import operator

def evaluate(x):
	return x+(1/x)

def bin_to_dec(a):
    global g
    dec=0
    for i in range(g):
        dec+=a[i]*(2**(g-i-1))
    return dec

def get_genes(g):
	return [r.randint(0,1) for i in range(g)]

def select(population,p):
	selected=[]
	sr=int(0.6*p)
	while sr>0:
		r1,r2=r.randint(0,p-1),r.randint(0,p-1)
		if r1 in selected or r2 in selected :
			continue
		else:
			if evaluate(bin_to_dec(population[r1]))>evaluate(bin_to_dec(population[r2])):
				selected.append(r1)
			else:
				selected.append(r2)
		sr-=1
	return selected

def crossover(population,selected,g):
	bound=int(0.8*g)
	for i in range(0,len(selected)-1,2):
		c1=list(population[selected[i]])
		c2=list(population[selected[i+1]])
		for j in range(bound):
			c1[j],c2[j]=c2[j],c1[j]
		population.append(c1)
		population.append(c2)
	return population

def mutate(population,g):
	tot=len(population)
	mu=int(0.1*(tot))
	for i in range(mu):
		f=r.randint(0,tot-1)
		gen=r.randint(0,g-1)
		if population[f][gen]==1 :
			population[f][gen]=0
		else:
			population[f][gen]=1
	return population

def fitness_func(population,p):
	fit={}
	count=0
	new_pop=[]
	k=len(population)
	for i in range(k):
		fit[i]=evaluate(bin_to_dec(population[i]))
	fit=sorted(fit.items(),key=operator.itemgetter(1))
	for i in range(k-1,-1,-1):
		if count==p:
			break
		new_pop.append(population[fit[i][0]])
		count+=1
	population=list(new_pop)
	return population,fit

p=int(input("Enter population size: "))
g=int(input("Enter no.of genes: "))
population=[get_genes(g) for i in range(p)]
it=100

while it:
	selected=select(population,p)
	population=crossover(population,selected,g)
	population=mutate(population,g)
	population,fit=fitness_func(population,p)
	it-=1
print(fit)