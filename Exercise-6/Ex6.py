# Import libraries and modules
import numpy as np
# *********************************************************part (1) and (2)**********************************************************************************************************************************************
# Define the three lists as rows
row1 = [4, 5, 0, 5, 1, 0, 3, 2]
row2 = [0, 3, 4, 3, 1, 2, 1, 0]
row3 = [2, 0, 1, 3, 0, 4, 5, 3]

# Create the matrix using NumPy with data type as float
initial_matrix = np.array([row1, row2, row3], dtype=float)

# Print the matrix
print("Initial Matrix:")
print(initial_matrix)
print()  

# Jaccard distance function
def jaccard_distance(row1, row2):
    intersection = sum(1 for i, j in zip(row1, row2) if i and j)
    union = sum(1 for i, j in zip(row1, row2) if i or j)
    distance = 1 - (intersection / union)
    return distance

# Cosine similarity function
def cosine_similarity(rowi, rowj):
    dot_product = np.dot(rowi, rowj)
    magnitudei = np.linalg.norm(rowi)
    magnitudej = np.linalg.norm(rowj)
    if magnitudei != 0 and magnitudej != 0:
        return dot_product / (magnitudei * magnitudej)
    else:
        return 0

# list of all pair edges (records)
all_edges_list0 =[]

# Calculate Jaccard distance and cosine similarity between users
for i in range(3):
    for j in range(1, 3):
        if ((i, j) not in all_edges_list0) and (i != j) and ((j, i) not in all_edges_list0):
            all_edges_list0.append((i, j))
            print(f"({i}, {j}), cosine_similarity for initial matrix : ", cosine_similarity(initial_matrix[i], initial_matrix[j]), " jaccard_distance for initial matrix : ", jaccard_distance(initial_matrix[i], initial_matrix[j]))
            print()  

# **************************************************part (3) and (4)***********************************************************************************************************************************************
# Change elements of matrix based on the condition:
modified_matrix = np.where(initial_matrix >= 3, 1, 0)

# Print the modified matrix:
print("Modified Matrix:")
print(modified_matrix)
print()  

# list of all pair edges (records)
all_edges_list1 =[]

# Calculate Jaccard distance and cosine similarity between users on modified matrix
for i in range(3):
    for j in range(1, 3):
        if ((i, j) not in all_edges_list1) and (i != j) and ((j, i) not in all_edges_list1):
            all_edges_list1.append((i, j))
            print(f"({i}, {j}), cosine_similarity for modified matrix : ", cosine_similarity(modified_matrix[i], modified_matrix[j]), " jaccard_distance for modified matrix : ", jaccard_distance(modified_matrix[i], modified_matrix[j]))
            print()  

# **************************************************part (5) and (6)***********************************************************************************************************************************************
# Normalize the matrix by subtracting the average value for each row
normalized_matrix = np.copy(initial_matrix)  # Create a copy of the initial matrix

# Iterate over each row
for i in range(normalized_matrix.shape[0]):
    row = normalized_matrix[i]
    row_average = np.mean(row[row != 0])  # Calculate the average of non-zero elements in the row
    row[row != 0] -= row_average  # Subtract the average from non-zero elements

# Print the normalized matrix
print("Normalized Matrix:")
print(normalized_matrix)
print()  

# list of all pair edges (records)
all_edges_list2 =[]

# Calculate Jaccard distance and cosine similarity between users on normalized matrix
for i in range(3):
    for j in range(1, 3):
        if ((i, j) not in all_edges_list2) and (i != j) and ((j, i) not in all_edges_list2):
            all_edges_list2.append((i, j))
            print(f"({i}, {j}), cosine_similarity for normalized matrix : ", cosine_similarity(normalized_matrix[i], normalized_matrix[j]), " jaccard_distance for normalized matrix : ", jaccard_distance(normalized_matrix[i], normalized_matrix[j]))
            print()  