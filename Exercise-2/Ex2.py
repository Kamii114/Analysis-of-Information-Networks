#Libraries:
from igraph import *
import matplotlib.pyplot as plt
import math
import numpy as np

#Creating a Random Erdos Renyi Network with 1000 Vertices and Probability of 0.002:
g1 = Graph.Erdos_Renyi(n=1000, p=0.002, directed=False, loops=False)

#Calculating K_Mean:
sum=0
degree_list=[]
for i in range(len(Graph.degree(g1))):
    sum += (Graph.degree(g1))[i]

k_mean = sum/1000
print("K_mean is: ", k_mean)

#Calculating the Real Value of K_Max:
print("The real K_Max is:",Graph.maxdegree(g1))

#Calculating K_max from Formula:
K_max=0
result_1=round((1/(1000*math.exp(-k_mean))),2)

for i in range(0,999):
    result_2 = round(int(pow(k_mean, i+1)) / math.factorial(i+1),2)
    if result_1 in np.arange(result_2 , result_2 + 0.05) or result_1 in np.linspace(result_2 - 0.05 , result_2):
        K_max = i             
    
print("K_Max based on Formula is: ",K_max)

#Calculating S:
x=np.linspace(0,2,200)

y=x
z= 1 - np.exp(-1*1.7*x)

plt.title('What is S?')
plt.xlabel('S')


plt.grid()
plt.scatter(x,z,s=10)
plt.scatter(x,y,s=10)
idx = np.argwhere(np.diff(np.sign(y - z))).flatten()
plt.plot(x[idx], y[idx], 'ro')
print("S = ",idx[-1],"%")
plt.show()


