def fullSolution(U, A, B, C):
    U = list(U)
    A = list(A)
    B = list(B)
    C = list(C)
    notA = []
    Z = []
    result = []
    for i in U:
        if i not in A:
            notA.append(i)
    for j in notA:
        if j in B:
            Z.append(j)
    for j in A:
        if j not in Z:
            Z.append(j)
    for j in Z:
        if j not in C:
            result.append(j)
    result.sort()
    return set(result)
