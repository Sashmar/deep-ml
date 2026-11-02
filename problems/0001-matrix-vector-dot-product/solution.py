def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	c = []

	if(len(a[0]) != len(b)):
		c.append(-1)
		return c


	for row in range(len(a)):
		sum = 0
		i = 0
		for col in range(len(a[0])):
			sum += a[row][col] * b[i]
			i += 1
		
		c.append(sum)

	return c