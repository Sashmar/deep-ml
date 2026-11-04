import numpy as np

def make_diagonal(x):
	# Your code here
	rows = len(x)

	matrix = [[0 for _ in range(rows)] for _ in range(rows)]

	for i in range(len(x)):
		matrix[i][i] = x[i]

	
	return matrix