import matplotlib.pyplot as plt
from dijkstra import tt
dtt = tt
from bellmanford import tt
btt = tt
import numpy 

alg = ['DIJKSTRA' , 'BELLMAN-FORD']
tt = [dtt, btt]
ypos = numpy.arrange(len(alg))
plt.xsticks(ypos,alg)
plt.ylabel("Time(s)")
plt.xlabel("Dijkstra vs Bellman-Ford")
plt.title("DAA Project: Team 12")
l = plt.bar(ypos, tt)
l[0].set_color('r')
plt.legend()
plt.show()

