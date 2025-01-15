# Given data with very few nonzero values, we want to efficiently represent it.

# Create a sparse matrix

# load libraries
import numpy as np
from scipy import sparse

# create a matrix
martix = np.array([[0, 0],
		[0, 1],
		[3, 0]])

# Create compressed sparse row (CSR) matrix
matrix_sparse = sparse.csr_matrix(matrix)

# view sparse matrix
print(matrix_sparse)


