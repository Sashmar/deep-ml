import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	rows = len(a)
	cols = len(a[0])
	c = []
	l = []
	reshaped_matrix = []
	r1 = new_shape[0]
	c1 = new_shape[1]
	if rows * cols != r1 * c1:
		return c
	for i in range(rows):
		for j in range(cols):
			c.append(a[i][j])

	for i in c:
		l.append(i)

		if len(l) == c1:
			reshaped_matrix.append(l)
			l = []



	
	return reshaped_matrix