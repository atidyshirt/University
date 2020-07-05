num_calls = 0  # Global counter of mat_mul calls

def mat_mul(m1, m2):
    """Return m1 * m2 where m1 and m2 are square matrices of numbers, represented
       as lists of lists.
    """
    global num_calls # Counter of calls (for marking)
    num_calls += 1   # Increment the count of calls
    n = len(m1)    # Size of the matrix
    assert len(m1[0]) == n and len(m2) == n and len(m2[0]) == n
    mprod = [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)]
    return mprod

def mat_power(m, p):
    product = m
    if p == 1:
        return product
    if p % 2 == 0:
        res = mat_power(m, p/2)
        return mat_mul(res, res)
    else:
        return mat_mul(mat_power(m, p-1), m)

m = [[1, 2, 3], [0, -1, 3], [2, 4, 1]]
num_calls = 0
m20 = mat_power(m, 20)
print(m20, num_calls)
