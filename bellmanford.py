import numpy
import time
import sys

def BellmanFord(graph, V, E, src, edge) :
    dist=[sys.maxsize] * V
    dist[src] = 0
    flag = True

    for i in range(V - 1) :
        for j in range(E) :
            u = edge[j][0]
            v = edge[j][1]
            if (dist[u] + graph[u][v]) < dist[v] :
                dist[v] = dist[u] + graph[u][v]
    
    for i in range(E) :
        u = edge[i][0]
        v = edge[i][1]
        if dist[u] + graph[u][v] < dist[v] :
            flag = False
    
    if flag :
        for i in range(V) :
            print("Vertex {} :-> cost = {}".format(i, dist[i]))
        
        return flag
        
if __name__ == "__main__" :
    V = int(input("Enter the number of vertices : "))
    k = 0
    rows, cols = (20, 2)
    edge = [[0 for i in range(cols)] for j in range(rows)] 
    assert V > 0, "The number of vertices should be more than zero"
    print("Enter the elements in the matrix")
    elements = list(map(int,input().split()))
    matrix = numpy.array(elements).reshape(V,V)
    for i in range(V) :
        for j in range(V) :
            if matrix[i][j] != 0 :
                edge[k][0] = i
                k += 1
                edge[k][1] = j
    #print("k value: {}".format(k))
    print("The given adjacency matrix is : ")
    print(matrix)
    print("Please enter the source vertex ")
    source = int(input())
    start = time.process_time()
    if BellmanFord(matrix, V, k, source, edge) :
        print("No negaative weight cycle")
    else :
        print("Negative weight cycle exists")
    end = time.process_time()
    print("Time elapsed during execution : {}".format(end-start))
