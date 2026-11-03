def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if len(a[0]) != len(b):
        return -1

    row1 = len(a)
    col1 = len(a[0])

    row2 = len(b)
    col2 = len(b[0])

    c =  [[0 for _ in range(col2)] for _ in range(row1)]

    for i in range(len(a)):
        k = 0
        j = 0
        s = 0
        g = 0
        f = 0
        while j < len(a[0]):
            s += (a[i][j] * b[g][f])
            g += 1

            if j == len(a[0]) -1:
                g = 0
                c[i][f] = s
                f += 1
                s = 0
                if f < col2:
                    j = 0
                else:
                    break
            else:
                j += 1

                
    return c