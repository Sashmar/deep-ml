def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []

	numr = len(matrix)
	numc = len(matrix[0])

	if mode == 'column':
		for col in range(numc):
			mean = 0
			for row in range(numr):
				mean += matrix[row][col]
			means.append(mean/numr)

	else:
		for row in range(numr):
			mean = 0
			for col in range(numc):
				mean += matrix[row][col]
			means.append(mean/numc)

	return means