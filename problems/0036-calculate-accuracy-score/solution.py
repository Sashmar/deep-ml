import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	count = 0
	for yt, yp in zip(y_true, y_pred):
		if yt == yp:
			count += 1

	s = y_pred.size
	return count / s 