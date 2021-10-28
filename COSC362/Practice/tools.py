# write a function to find the inverse of a number modulo n

def inverse_modulo(a, n):
    """
    Find the inverse of a number modulo n
    """
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        for i in range(1, n):
            if (a * i) % n == 1:
                return i

print(3, 17, inverse_modulo(3, 17))