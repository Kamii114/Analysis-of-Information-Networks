#Libraries:
from igraph import *
import matplotlib.pyplot as plt
import math
import numpy

#Creating a Random Erdos Renyi Network with 1000 Vertices and Probability of 0.005:
g1 = Graph.Erdos_Renyi(n=1000, p=0.005, directed=False, loops=False)


#Displaying the Number of Nodes and the Number of Edges:
print("(The Number of Nodes,The Number of Edges): ", g1.summary())


#Visualization of the Random Network with igraph Library:

plot(
    g1,
    vertex_size=20,
    vertex_color=['deeppink' for v in g1.vs],
    vertex_label=range(g1.vcount()),
    edge_width=[1],
    edge_color=['black'],
    target= 'Random_Network.png'
)
plt.show()

#Visualization of the Random Network with Gephi:
g1.write_graphml("Random_Graph_Visualization.graphml")

#Calculating the Diameter of Network:
print("The diameter of network: ",Graph.diameter(g1))

#Calculating the Average Path Length:
print("The Real Average Path Length of the Network is: ",Graph.average_path_length(g1))

# Calculating the Global clustering coefficient: 
print("The Global Clustering Coefficient of the Network is: ",Graph.transitivity_undirected(g1))

#Calculating the Average clustering coefficient:
print("The Average Clustering Coefficient of the Network is: ",Graph.transitivity_avglocal_undirected(g1))

#Plotting the Degree Distribution Diagram:(Count)

title_font = {'fontname':'serif','color':  'darkred','weight': 'bold','size': 12}
axis_font = {'fontname':'serif','color':  'black','weight': 'bold','size': 10}
plt.hist(g1.degree(), bins=20)
plt.xlabel('Degree',**axis_font)
plt.ylabel('Count',**axis_font)
plt.xticks(rotation=90)
plt.title("Degree_Distribution_Count_log",**title_font)
plt.xscale("log")
plt.yscale("log")
plt.savefig("Degree_Distribution_Count_log.png")
plt.show()

#Plotting the Degree Distribution Diagram:(Poisson)

Expected_Value_of_K=999*0.005
p=[]
for i in range(len(g1.degree())):
    p.append((numpy.power(math.e,-Expected_Value_of_K))*(numpy.power(Expected_Value_of_K,((g1.degree())[i]))/(numpy.math.factorial((g1.degree())[i]))))

plt.scatter(g1.degree(), p)
plt.xlabel('Degree (K)',**axis_font)
plt.ylabel('P(k)',**axis_font)
plt.title("Degree_Distribution_Poisson_log",**title_font)
plt.xscale("log")
plt.yscale("log")
plt.savefig("Degree_Distribution_Poisson_log.png")
plt.show()

#Calculating the Average Path Length Based on Formula:
sum=0
degree_list=[]
for i in range(len(Graph.degree(g1))):
    sum += (Graph.degree(g1))[i]

k_mean = sum/1000
v = Graph.vcount(g1)

average_distance = numpy.log(v) / numpy.log(k_mean)
print("The Average Path Length of the Network Based on the Formula is: ",average_distance)


