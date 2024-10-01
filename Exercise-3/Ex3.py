#Libraries:
from igraph import *
import igraph as ig
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# read zachary dataset file
zachary_graph = Graph.Read_Ncol('ZacharyDataset.txt', directed=False)

# Creating the Zachary Club Network from dataset.txt:
vertex_lables = []
for i in range(0,34):
    vertex_lables.append(i)

# Visualization of the Zachary Club Network with igraph library:
plot(
    zachary_graph,
    vertex_size=20,
    vertex_color=['deeppink' for v in zachary_graph.vs],
    vertex_label=range(zachary_graph.vcount()),
    edge_width=[1],
    edge_color=['black'],
    target= 'ZacharyClub_igraph_visualization.png'
)
plt.show()

# Plotting the Degree Distribution Diagram on a log-log scale:
title_font = {'fontname':'serif','color':  'darkred','weight': 'bold','size': 12}
axis_font = {'fontname':'serif','color':  'black','weight': 'bold','size': 10}
plt.hist(zachary_graph.degree(), bins=range(max(zachary_graph.degree())), align='left', rwidth=0.7)
plt.xlabel('Degree',**axis_font)
plt.ylabel('Count',**axis_font)
plt.xticks(rotation=90)
plt.title("ZacharyClub_Degree_Distribution_log",**title_font)
plt.xscale("log")
plt.yscale("log")
plt.savefig("ZacharyClub_Degree_Distribution_log.png")
plt.show()

# Get the degrees of the nodes
degrees = zachary_graph.degree()
degrees = sorted(degrees)
print("degrees = ", degrees)

#Making a list of all our distinct K's and a list of their Probabilities:
distinct_k_list=[]
Probability_k_list=[]
iteration_k_list=[]

for x in degrees:
    x_count=0
    for y in degrees:
        if x==y:
            x_count +=1

            if x not in distinct_k_list:
              distinct_k_list.append(x)

    # print(x_count)
    # print(distinct_k_list)
    # print("probability of ", x ," is : ", x_count/34)
    for p in distinct_k_list:
        if p not in iteration_k_list:
            iteration_k_list.append(p) 
            Probability_k_list.append((x_count/ zachary_graph.vcount()))
    # print(Probability_k_list)

# Making our list of distinct K's and their Probablities have a len of 34 so that we can use them later to make a matrix:
count34 = 0
distinct_k_list_34=[]
Probability_k_list_34=[]
for i in range(0,34):
    if i in distinct_k_list:
       distinct_k_list_34.append(i)
       Probability_k_list_34.append(Probability_k_list[count34])
       count34 +=1
    else:
        distinct_k_list_34.append(0)
        Probability_k_list_34.append(0)


# Calculate kpk
kpk = np.multiply(distinct_k_list_34, Probability_k_list_34)

# Calculate <k> (average degree of network):
average_degree = np.mean(degrees)

# Calculate qk
qk = kpk / average_degree

# Calculate the probability matrix (eij matrix)
eij_matrix = np.zeros((len(degrees), len(degrees)))

for i in degrees:
    for j in degrees:
        eij_matrix[i, j] = qk[i] * qk[j]


# Plotting eij matrix's diagram:
plt.imshow(eij_matrix, cmap="hot", origin="upper")
plt.colorbar()
plt.xlabel("j")
plt.ylabel("i")
plt.title("eij Matrix")
plt.savefig("eij Matrix.png")
plt.show()

# Calculating Zachary network's knn:
zachary_graph_knn = Graph.knn(zachary_graph)
zachary_tuple1 = zachary_graph_knn[0]

# Plotting Knn_K diagram on a log-log scale and running a line of best fit throough our data points:
title_font = {'fontname':'serif','color':  'darkred','weight': 'bold','size': 12}
axis_font = {'fontname':'serif','color':  'black','weight': 'bold','size': 10}
slope, intercept, r_value, p_value, std_err = stats.linregress(zachary_graph.degree(), zachary_tuple1)
x_line = np.array([1 , 17])
y_line = intercept + slope * x_line
plt.plot(x_line, y_line, color='red', label='Line of Best Fit', linestyle='--', linewidth=3 )
plt.scatter(zachary_graph.degree(),zachary_tuple1)
plt.xlabel('K',**axis_font)
plt.ylabel('knn(k)',**axis_font)
plt.xscale("log")
plt.yscale("log")
plt.title("Knn(k)_k_log",**title_font)
plt.savefig("Knn(k)_k_log.png")
x=np.linspace(0,1,100) 
plt.show()

# Calculating the assortativity coefficient of zachary club network:
print(" Assortativity Coefficient of Zachary club is: ", Graph.assortativity_degree(zachary_graph))
