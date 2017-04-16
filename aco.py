import random as r
import math as m

def shortest_path(node,inv_dist,pheronome,n,dist):
	tabu_list=[node];distance=0;curr_node=node
	while len(tabu_list)<n:
		table={}
		for i in range(n):
			if i not in tabu_list:
				table[i]=pheronome[node][i]*(inv_dist[node][i]**2)
		sor=sorted(table.items(),key=lambda x:x[1],reverse=True)
		distance+=dist[node][sor[0][0]]
		node=sor[0][0]
		tabu_list.append(node)
	tabu_list.append(curr_node);distance+=dist[node][curr_node]
	return tabu_list,distance

def update(pheronome,tabu_list,dist):
	for i in range(len(tabu_list)-1):
		pheronome[tabu_list[i]][tabu_list[i+1]]+=1/dist
	for i in range(len(pheronome)):
		for j in range(len(pheronome)):
			pheronome[i][j]=0.5*pheronome[i][j]

def main():
	n=int(input("Enter number of cities: "))
	distances=[[float(i) for i in input("Enter distances: ").split(' ')] for j in range(n)]
	pheronome=[[0.2]*n for i in range(n)]
	inv_distances=[]
	for i in range(n):
		temp=[]
		for j in range(n):
			if i!=j:
				temp.append(1/distances[i][j])
			else:
				temp.append(100000000)
		inv_distances.append(temp)
	best_dist=100000;prev_dist=1000;best_path=[];it=2
	while it>0:
		for i in range(n):
			curr_best_path,curr_best_dist=shortest_path(0,inv_distances,pheronome,n,distances)
			#print(curr_best_dist,curr_best_path)
			if curr_best_dist<best_dist:
				best_path,best_dist=curr_best_path,curr_best_dist
		update(pheronome,best_path,best_dist)
		it-=1
	print(best_dist,best_path)

if __name__=="__main__":
	main()