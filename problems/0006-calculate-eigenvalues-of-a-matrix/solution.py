def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = 0

	for i in range(2):
		trace += matrix[i][i]

	eigenvalues = []

	det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

	d = trace ** 2 - 4 * 1 * det

	eigenvalues.append((trace + d ** 0.5) / 2 * 1)
	eigenvalues.append((trace - d ** 0.5) / 2 * 1) 
	return eigenvalues