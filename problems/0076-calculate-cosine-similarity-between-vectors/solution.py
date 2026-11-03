import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.size == v2.size and v1.size > 0 and v2.size > 0:
		v1v2 = np.dot(v1, v2)

		v1v1 = np.power(v1, 2)
		s1 = sum(v1v1)
		sq1 = np.sqrt(s1)

		v2v2 = np.power(v2, 2)
		s2 = sum(v2v2)
		sq2 = np.sqrt(s2)

		return v1v2 / (sq1 * sq2)
	pass