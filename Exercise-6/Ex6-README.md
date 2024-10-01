# Analysis of Information Networks

# Exercise 6: Recommender System

## Problem Statement

The objective of this exercise is to analyze a rating matrix representing ratings given by three users (A, B, and C) to eight items (a to h) on a scale of 1 to 5 stars. Based on this matrix, we will perform various calculations to evaluate user similarity and recommend items.

### Rating Matrix

![Rating Matrix](Exercise-6/RatingMatrix.png)

## Tasks

1. **Calculate Jaccard Distance:** Compute the Jaccard distance between each pair of users based on their ratings.

2. **Calculate Cosine Similarity:** Repeat the previous calculation using cosine similarity instead of Jaccard distance.

3. **Binary Rating Conversion:** Consider ratings of 3, 4, and 5 as 1, and ratings of 1 and 2, as well as empty ratings, as 0. Compute the Jaccard distance between each pair of users using this binary representation.

4. **Binary Cosine Similarity:** Repeat the previous calculation using cosine similarity.

5. **Normalization:** Normalize the rating matrix by subtracting the average rating of each user from their ratings, ignoring empty inputs.

6. **Normalized Cosine Similarity:** Using the normalized matrix, compute the cosine similarity between each pair of users.

## Expected Outcomes

- A comprehensive report of the calculated Jaccard distances and cosine similarities for the initial, modified, and normalized matrices.
- Insights into user similarity based on different distance and similarity metrics.
- A better understanding of how normalization impacts the similarity calculations.
