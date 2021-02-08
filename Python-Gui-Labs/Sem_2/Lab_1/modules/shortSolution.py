def shortSolution(A, B, C):
    # U
    A = list(A)
    B = list(B)
    Z = []
    for i in A:
        Z.append(i)
    for i in B:
        if i not in Z:
            Z.append(i)
    Z.sort()
    # \
    result = []
    C = list(C)
    for el in Z:
        if not el in C:
            result.append(el)
        continue
    result.sort()
    return set(result)