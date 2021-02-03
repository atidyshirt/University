def fact(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res

# Applying the formula
def count_heads(n, r):
    output = fact(n) / (fact(r) * fact(n - r))
    output = output / (pow(2, n))
    return output

# Driver code
n = 10
r = 7

# Call count_heads with n and r
print(count_heads(n, r))
