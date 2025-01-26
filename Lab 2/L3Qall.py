import numpy as np

# 1. Solve linear equations Ax = B
A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])
print("Solution:", np.linalg.solve(A, B))

# 2. Determinant of 3x3 matrix
matrix = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print("Determinant:", np.linalg.det(matrix))

# 3. Eigenvalues and eigenvectors of 2x2 matrix
matrix = np.array([[4, -2], [1, 1]])
vals, vecs = np.linalg.eig(matrix)
print("Eigenvalues:", vals)
print("Eigenvectors:\n", vecs)

# 4. Sort 2D array by 2nd column
array = np.array([[1, 3, 2], [4, 1, 5], [7, 2, 8]])
print("Sorted by 2nd column:\n", array[array[:, 1].argsort()])

# 5. Matrix multiplication
m1, m2 = np.array([[1, 2], [3, 4]]), np.array([[2, 0], [1, 3]])
print("Matrix multiplication:\n", np.dot(m1, m2))

# 6. Max and min in 2D array
array = np.array([[3, 5, 1], [9, 2, 8], [6, 7, 4]])
print("Max:", np.max(array), "Min:", np.min(array))
