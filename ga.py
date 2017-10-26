from math import *
import random

func = input("Enter function: ")
f = lambda x : eval(func)


def selection(pop):
	selected = []
	p = len(pop)
	for i in range(int(0.8*p)):
		p1, p2 = [random.randint(0,p-1) for i in range(2)]
		if f(pop[p1]) < f(pop[p2]) :
			selected.append(pop[p1])
	return selected


def crossover(select):
	mu = 20
	child = []
	for i in range(0, len(select)-2, 2):
		r = random.uniform(0,1)
		b = (2*r)**(1/(mu+1)) if r <= 0.5 else (1/2*(1-r))**(1/(mu+1))
		try:
			child1 = 0.5*((1+b)*select[i] + (1-b)*select[i+1])
			child2 = 0.5*((1-b)*select[i] + (1+b)*select[i+1])
		except IndexError as e:
			print(e, i)
		child.extend([child1, child2])
	return child


def select_best(total, p):
	fit = map(f, total)
	a = dict(zip(total, fit))
	sorted_dict = dict(sorted(a.items(), key=lambda x: x[1]))
	return list(sorted_dict.keys())[:p] 


def mutation(child):
	n = 20
	for i in range(int(0.2*len(child))):
		r = random.uniform(0, 1)
		d = (2*r)**(1/(n+1)) - 1 if r <=0.5 else 1 - (2*(1 - r))**(1/ (n+1))
		m = random.randint(0, len(child)-1)
		child[m] += d


def main() :
	p = int(input("Enter population size: "))
	l, r = [float(i) for i in input("Enter range: ").strip().split(' ')]
	population = []

	for i in range(p):
		population.append(random.uniform(l, r))

	it = 400
	while it > 0:
		selected = selection(population)
		children = crossover(selected)
		mutation(children)
		population = select_best(population + children, p)
		it -= 1

	print(f(population[0]))

if __name__ == "__main__":
	main()