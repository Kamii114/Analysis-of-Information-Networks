#Libraries:
from igraph import *
import igraph as ig
import matplotlib.pyplot as plt
import numpy as np

# read zachary dataset file
zachary_graph = Graph.Read_Ncol('ZacharyDataset.txt', directed=False)

# Creating the Zachary Club Network from dataset.txt:
vertex_lables = []
for i in range(0,34):
    vertex_lables.append(i)

# Get the degrees of the nodes
degrees = zachary_graph.degree()

# Calculate <k> (average degree of network):
kmean_first_moment = np.mean(degrees)
print(kmean_first_moment)

#Calculating <k^2>:
sum=0
degree_list=[]
for i in range(len(Graph.degree(zachary_graph))):
    sum += pow((Graph.degree(zachary_graph))[i] , 2)
    # print(sum) 
k2mean_Second_moment = sum/34
print(k2mean_Second_moment)

#Taking β and μ values from user:
beta = float(input("Enter β value: "))
miu = float(input("Enter μ value: "))
        
#Calculating T_si, T_sis, T_sir:
T_si = np.divide(kmean_first_moment, np.multiply(beta, np.subtract(k2mean_Second_moment, kmean_first_moment)))
print("T_si is: ",T_si)

T_sis = np.divide(kmean_first_moment, np.subtract(np.multiply(beta, k2mean_Second_moment), np.multiply(miu, kmean_first_moment)))
print("T_sis is: ",T_sis)

T_sir = np.divide(kmean_first_moment, np.subtract(np.multiply(beta, k2mean_Second_moment), np.multiply(np.add(miu, beta), kmean_first_moment)))
print("T_sir is: ",T_sir)

#Calculating λ, λc_sis, λc_sir:
landa = np.divide(beta,miu)
print("λ is: ",landa)

landac_sis = np.divide(kmean_first_moment,k2mean_Second_moment)
print("λc_sis is: ",landac_sis)

landac_sir = np.divide(1, np.subtract(np.divide(k2mean_Second_moment, kmean_first_moment), 1))
print("λc_sir is: ",landac_sir)

