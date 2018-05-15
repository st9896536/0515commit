#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:40:45 2017

@author: Rong
"""

# Python program for Dijkstra's single source shortest
# path algorithm. The program is for adjacency matrix
# representation of the graph

from collections import defaultdict
import numpy as np

#定義class graph
class Graph:

	# A utility function to find the vertex with minimum dist value, from
	# the set of vertices still in queue
	def minDistance(self,dist,queue):
		# 初始值minimum and min_index 都先設成-1
		minimum = float("Inf")
		min_index = -1
		#從disk array裡面,挑出一個有min value 且還在queue裡面
		for i in range(len(dist)):
			if dist[i] < minimum and i in queue:
				minimum = dist[i]
				min_index = i
		return min_index


	# Function to print shortest path from source to j
	# using parent array
	def printPath(self, parent, j):
		if parent[j] == -1 : #Base Case : If j is source
			print(j)
			return j
		self.printPath(parent , parent[j])
		print(j)
		

	# A utility function to print the constructed distance
	# array
	def printSolution(self, dist, parent, start):
		print("Vertex \t\tDistance from Source\tPath")
		for i in range(1, len(dist)):
			print("\n%d --> %d \t\t%d \t\t\t\t\t" % (start, i, dist[i])),self.printPath(parent,i)


	def dijkstra(self, graph, start):

		row = len(graph)
		col = len(graph[0])

		# The output array. dist[i] 為最小距離 從 start 到 i
		# 初始值先設定所有distance為無限大 
		dist = [float("Inf")] * row

		#Parent array to store shortest path tree
		parent = [-1] * row

		# 節點自己到自己都會是0
		dist[start] = 0
	
		# 把所有的節點加進去queue裡
		queue = []
		for i in range(row):
			queue.append(i)
			
		#找所有節點的最短路徑
		while queue:

			# Pick the minimum dist vertex from the set of vertices
			# still in queue
			u = self.minDistance(dist,queue) 

			# 刪除最小值 
			queue.remove(u)

			# Update dist value and parent index of the adjacent vertices of
			# the picked vertex. Consider only those vertices which are still in
			# queue
          # 更新dist 距離 和 parent index 
			for i in range(col):
				if graph[u][i] and i in queue:
					if dist[u] + graph[u][i] < dist[i]:
						dist[i] = dist[u] + graph[u][i]
						parent[i] = u


		# print the constructed distance array
		self.printSolution(dist,parent,start)

g= Graph()

"""
routers = int(input("routers(please input 1 ~ 5): ")) #let user enter routers num
graph = np.zeros((routers,routers)) #先設一個空的graph array

#一開始由user輸入初始的link cost
for i in range(routers):
    for j in range(routers):
        graph[i][j] = int(input("router %d 到 router %d 的距離: " % (i+1 ,j+1) ))
"""

#再讓user選擇要從哪個router開始走
start = int(input("start router: "))
end = int(input("destnation router: "))

#Print the solution
g.dijkstra(graph,start) 


#This code is contributed by Neelam Yadav
