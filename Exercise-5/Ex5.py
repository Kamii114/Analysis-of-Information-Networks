
# Import libraries and modules
from igraph import *
import matplotlib.pyplot as plt
import math
import numpy
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# ********* Section1 -->> Calculate three criteria (common neighbors, jaccard coefficient, Adamic/Adar) for link prediction ******************
# read Zachary's Club dataset file
g = Graph.Read_Ncol('zachary_dataset.txt', directed=False)

# define a list that store nodes ID (1 ~ 34)
labels = []
for i in range(0,34):
    labels.append(i)

# plot undirected graph and save as .svg format
plot(g,
        vertex_size=40,
        vertex_color=['yellowgreen', 'goldenrod'],
        vertex_label=labels,
        edge_width=[1],
        edge_color=['black'],
        target='zachary_club.png'
        )

# Display the Zachary's Club graph using matplotlib
img = plt.imread('zachary_club.png')
plt.imshow(img)
plt.axis('off')
plt.show()

# define common neighbors function as |r(x)∩ r(y)|
def common_neighbors1(g, i, j):
    return len(set(g.neighbors(i)).intersection(set(g.neighbors(j))))

# define jaccard coefficient function as |r(x)∩ r(y)|/|r(x) ∪ r(y)|
def jaccard_coefficient1(g, i, j):
    intersection = set(g.neighbors(i)).intersection(set(g.neighbors(j)))
    union = set(g.neighbors(i)).union(set(g.neighbors(j)))
    if len(union) > 0:
        return len(intersection) / len(union)
    else:
        return 0

# define Adamic/Adar function as |r(x)∩ r(y)|/|r(x) ∪ r(y)|
def adamic_adar1(g, i, j):
    adamic_adar_index = 0
    for z in (set(g.neighbors(i)).intersection(set(g.neighbors(j)))):
        degree = g.degree(z)
        if degree > 1:
            adamic_adar_index += (1 / math.log(degree))
    return adamic_adar_index


# list of all pair edges (records)
all_edges_list =[]

# print pair of nodes and their common neighbors, jaccard coefficient and Adamic/Adar
for  i in range(0,34):
    for  j in range(0,34):
        if ((i,j) not in  all_edges_list) and (i!=j) and ((j,i) not in  all_edges_list):
            all_edges_list.append((i,j))
            print(f"({i}, {j}), common_neighbors : ",common_neighbors1(g, i, j), " jaccard_coefficient : ", jaccard_coefficient1(g, i, j), " adamic_adar : ",adamic_adar1(g, i, j))

# *********************************************************************************************************************************************************************************



# ***************************** Link Prediction section *************************************
# Step 1: Prepare the Data
# Extract positive and negative edges (positive edges are edges that exist in the graph, and negative edges are edges that don't exist)
positive_edges = g.get_edgelist()
all_edges = [(i, j) for i in range(g.vcount()) for j in range(i+1, g.vcount())]
negative_edges = list(set(all_edges) - set(positive_edges))
negative_edges = negative_edges[:len(positive_edges)]

# Step 2: Extract Features (common_neighbors, jaccard_coefficient, adamic_adar_index)
# Extract feature values for each pair of nodes in the training data
X = [
    [
        common_neighbors1(g, edge[0], edge[1]),
        jaccard_coefficient1(g, edge[0], edge[1]),
        adamic_adar1(g, edge[0], edge[1])
    ]
    for edge in positive_edges + negative_edges
]

print (X)

# Step 3: Prepare the Training Data
# Combine positive and negative examples with their feature values
y = [1] * len(positive_edges) + [0] * len(negative_edges)

# Split the dataset into features (X) and target labels (y) (80 percent train and 20 percent test data)
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=42)


# Step 4: Train the Decision Tree Classifier
# Create an instance of the decision tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier to the training data
clf.fit(X_train, y_train)


# Step 5: Make Predictions
# Extract feature values for node pairs to predict links for
X_pred = [
    [
        common_neighbors1(g, edge[0], edge[1]),
        jaccard_coefficient1(g, edge[0], edge[1]),
        adamic_adar1(g, edge[0], edge[1])
    ]
    for edge in [(0, 1), (8, 30), (2, 3), (4, 5), (32, 19)]
]

# Use the trained decision tree classifier to predict link presence
y_pred = clf.predict(X_test)

# Calculate accuracy and error
accuracy = accuracy_score(y_test, y_pred)
error = 1 - accuracy

# Print accuracy and error
print("Accuracy:", accuracy)
print("Error:", error)

# Print actual labels (y_test) and predicted labels (y_pred)
print("Actual Labels (y_test):", y_test)
print("Predicted Labels (y_pred):", y_pred)

# Print classification report
print(classification_report(y_test, y_pred))
