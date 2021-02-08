def calculateZ(U, B, C):
    # not B
    X = list(C)
    U = list(U)
    B = list(B)
    Y = []
    result = []
    for i in U:
        if i not in B:
            Y.append(i)
    # Z = X\Y = C\ not B
    for i in X:
        if i not in Y:
            result.append(i)
    return set(result)