def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
	# Your code here

	if(z >= 0):
		return z

	else:
		if alpha == 0:
			return z * 0.01
		else:
			return z * alpha
	pass
