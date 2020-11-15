import sys
import numpy
import time

class Graph:
    
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for column in range(vertices)]for row in range(vertices)]
        
    def display(self,dist):
        print("Source\tDestination")
        for node in range(self.V):
            print(node," :-> ",dist[node])
    
    def min_dist(self,dist,sptSet):
        min=sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v]==False:
                min = dist[v]
                min_index=v
        return min_index
    def dijkstra(self,src):
        dist=[sys.maxsize]*self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for x in range(self.V):
            u=self.min_dist(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and \
                    sptSet[v] == False and \
                    dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.display(dist)
if __name__ == "__main__":
    V = int(input("Enter the number of vertices : "))
    g = Graph(V)
    assert V > 0, "The number of vertices should be more than zero"
    print("Enter the elements in the matrix")
    matrix = [[int(input()) for x in range (V)] for y in range(V)]
    print("The given adjacency matrix is : ")
    for i in range(V): 
        for j in range(V): 
            print(matrix[i][j],end=" ") 
        print() 
    g.graph = matrix
    source = int(input("Enter the source vertex : "))
    start = time.process_time()
    g.dijkstra(source); 
    end = time.process_time()
    tt = start-end
    print("Time elapsed during calculation : {}".format(tt))
