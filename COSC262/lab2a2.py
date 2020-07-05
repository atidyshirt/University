import sys
sys.setrecursionlimit(100000)

def dumbo_func(data, i=0):
    """Takes a list of numbers and does weird stuff with it"""
    if i >= len(data):
        return 0
    else:
        c = dumbo_func(data, i + 1)
        if (data[i] // 100) % 3 != 0:
            c += 1
        return c

def all_pairs(list1, list2, i=0):
    if i >= len(list1):
        return []
    return hello(list1[i], list2) + all_pairs(list1, list2, i +1)

def hello(number, list2, i=0):
    if i >= len(list2):
        return []
    return [(number, list2[i])] + hello(number, list2, i + 1)

def perms(items):

    if len(items) == 0:
        return [()]

    if len(items) == 1:
        return [tuple(items)]
    
    permutations = []

    for item in items:
        remaining = [i for i in items if i != item]
        recurse_perms = perms(remaining)

        for perm in recurse_perms:
            permutations.append(tuple([item]) + tuple(perm))

    return permutations

def combinations(items, r):
    if r > len(items):
        return []
    if r == 0:
        return [()]
    return recurse(items, r)
    


def recurse(items, n, combins=None):
    if combins == None:
        combins = []
    if len(items) == n:
        if combins.count(tuple(items)) == 0:
            combins.append(tuple(items))
        return combins
    
    for i in range(len(items)):
        remaining = items[:i] + items[i+1:]
        combos = recurse(remaining, n, combins)
    return combos



def matrix_multiply(A, B):
    num_rows, num_cols = len(A), len(B[0])
    C = [[0]*num_cols for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))
    return C


def matrix_power(A, n):
    if n == 1:
        return A
    elif n % 2 == 1:
        P = matrix_power(A, (n-1)/2)
        P = matrix_multiply(P, P)
        return matrix_multiply(P, A)
    else:
        P = matrix_power(A, n/2)
        return matrix_multiply(P, P)

def fib(n):
    if n == 0:
        return 0
    else:
        return matrix_power([[1, 1], [1, 0]], n)[0][1]




import math
def find_pit(seq, left=None, right=None):
    if left is None:
        left, right = 0, len(seq) - 1
    middle = math.floor((left + right)/2)
    if is_pit(seq, middle):
        return middle
    elif middle > 0 and seq[middle-1] <= seq[middle]:
        return find_pit(seq, left, middle - 1)
    else:
        return find_pit(seq, middle+1, right)

def is_pit(seq, index):
    return (len(seq)==1 and index==0 or
            index==0 and seq[0] <= seq[1] or
            index==len(seq)-1 and seq[-2]>=seq[-1] or
            seq[index-1] >= seq[index] <= seq[index+1])
