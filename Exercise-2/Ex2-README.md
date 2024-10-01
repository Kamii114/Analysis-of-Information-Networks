# Analysis of Information Networks

## Exercise 2: Calculating the Largest Component in a Random Network

### Problem Statement:
- **Task**: In a random network with 1000 nodes, choose a value for $\langle k \rangle$ (average degree) greater than one. The goals of this exercise are:
  1. **Phase Region**: Identify the phase region of the network based on the selected $\langle k \rangle$.
  2. **Maximum Degree**: Calculate the theoretical maximum degree $k_{\text{max}}$ and compare it with the observed value in the network.
  3. **Largest Connected Component**: Find the size $S$ of the largest connected component.

### Objectives:
- Determine the phase transition of the network.
- Calculate and compare theoretical vs. empirical values of $k_{\text{max}}$.
- Solve numerically to find the size of the largest component $S$.

### Steps:
1. **Generate a Random Network**: 
   - Using the Erdős–Rényi model with 1000 nodes and a specified edge formation probability.
   
2. **Calculate $k_{\text{mean}}$**:
   - Find the average degree $k_{\text{mean}}$ by calculating the sum of the degrees and dividing by the number of nodes.

3. **Find the Theoretical and Empirical $k_{\text{max}}$**:
   - Use a mathematical formula to compute the theoretical value of $k_{\text{max}}$, the maximum degree in the network.
   - Compare this with the actual maximum degree found in the generated network.

4. **Determine the Size of the Largest Component**:
   - Solve numerically using mathematical formulas and identify the largest connected component $S$.

### Outputs:
- **Average Degree** $\langle k \rangle$
- **Theoretical and Empirical Maximum Degree** $k_{\text{max}}$
- **Size of the Largest Component** $S$
