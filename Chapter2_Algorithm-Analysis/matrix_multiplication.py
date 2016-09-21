def multiply(A, B):
    """
    A of dimension x * y
    B of dimension y * z
    return C of dimension x * z
    """
    x = len(A)
    y = len(A[0])
    z = len(B[0])
    assert(y == len(B))

    C = [r[:] for r in [[0] * z] * x]

    for i in xrange(x):
        for j in xrange(z):
            for k in xrange(y):
                C[i][j] += (A[i][k] * B[k][j])

    return C


A = [[1, 2, 3],
     [2, 4, 6]]

B = [[1, 2],
     [2, 4],
     [3, 6]]

C = [[14, 28],
     [28, 56]]

assert(multiply(A, B) == C)
