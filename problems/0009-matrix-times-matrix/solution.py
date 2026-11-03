import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if len(a[0]) != len(b):
        return -1

    a1 = np.array(a)
    b1 = np.array(b)

    c = a1 @ b1

    c = c.tolist()

                
    return c