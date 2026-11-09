
from collections import Counter

def confusion_matrix(data):
	# Implement the function here

	tp = 0
	fn = 0
	fp = 0
	tn = 0
	for i in range(len(data)):
		if(data[i][0] == 1 and data[i][1] == 1):
			tp += 1
		elif(data[i][0] == 1 and data[i][1] == 0):
			fn += 1

		elif(data[i][0] == 0 and data[i][1] == 1):
			fp += 1

		elif(data[i][0] == 0 and data[i][1] == 0):
			tn += 1

	conma = [[0 for _ in range(2)] for _ in range(2)]

	conma[0][0] = tp
	conma[0][1] = fn
	conma[1][0] = fp
	conma[1][1] = tn

	return conma


	pass
