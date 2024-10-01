# Analysis of Information Networks

## Exercise 3: Degree Distribution and Assortativity in the Zachary Club Network

### Problem Statement:
- **Task**: In this exercise, we analyze the **Zachary Club Network** by computing various network metrics including the degree distribution, assortativity, and nearest-neighbor degree correlation. Additionally, we calculate and visualize the probability matrix (eij matrix) and plot important relationships such as the degree distribution and nearest-neighbor degree correlation on a log-log scale.

### Objectives:
1. **Visualize the Zachary Club Network**: Plot the network structure using the igraph library.
2. **Calculate and plot the degree distribution**: Display the degree distribution on a log-log scale to understand the spread of node degrees.
3. **Compute the eij matrix**: Calculate the probability matrix (eij matrix) based on node degrees and plot it as a heatmap.
4. **Plot the nearest-neighbor degree correlation**: Analyze the relationship between a node’s degree and the average degree of its neighbors.
5. **Determine the assortativity coefficient**: Compute the assortativity to assess the correlation of node degrees across network connections.

### Steps:
1. **Load the Zachary dataset**: The network is read from an external file `ZacharyDataset.txt` and visualized using the igraph library.
2. **Compute the degree distribution**:
   - Sort and plot the degree distribution of the network nodes on a log-log scale.
3. **Calculate the eij matrix**:
   - For each pair of nodes, calculate their corresponding probability value based on their degrees and visualize the matrix as a heatmap.
4. **Analyze the nearest-neighbor degree correlation**:
   - Calculate the nearest-neighbor degree correlation for each node and plot the relationship between node degree and the average degree of its neighbors on a log-log scale. A line of best fit is added for further analysis.
5. **Calculate assortativity**:
   - Compute the assortativity coefficient to measure the tendency of nodes to connect to others with similar degrees.

### Outputs:
- **Zachary Club Network Visualization**: Displays the structure of the network, with each node labeled and colored.
- **Degree Distribution Log-Log Plot**: A log-log plot of node degrees.
- **eij Matrix**: A heatmap visualization of the probability matrix.
- **Knn(k)_k Log-Log Plot**: A plot showing the relationship between node degrees and their neighbors’ average degrees.
- **Assortativity Coefficient**: A numerical value representing the assortativity of the network.

### References:
The Zachary Club Network dataset is a widely used social network dataset that models relationships among members of a karate club.
