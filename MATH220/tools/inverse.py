from math import *

# write a function to find the inverse of a number mod a given modulus

def inverse(a, m):
    gcd = euclid_algo(a, m)
    if gcd != 1:
        print("No inverse exists")
        return None
    else:
        return (m + a) % m

def gcd_working(Z, mod):
    result = []
    if len(Z) == 1:
        euclid_algo(Z[0], mod)
        return ""
    for item in Z:
        if euclid_algo(item, mod) == 1:
            result.append(item)
    print("--------------------------")
    print("gcd(" + str(result) + ", " + str(mod) + ")" + " Are all equal to 1")
    print("--------------------------")
    print("O(n) = " + str(mod))
    print("Z = " + str(Z))
    ans = "Z* = " + str(result)
    print("Length of Z* = " + str(len(result)))
    return ans

def euclid_algo(x, y):
    if x < y: # We want x >= y
        return euclid_algo(y, x)
    print("--------------------------")
    print()
    print("gcd({}, {})".format(y, x))
    while y != 0:
        print('%s = %s * %s + %s' % (x, floor(x/y), y, x % y))
        (x, y) = (y, x % y)

    print('gcd == %s' % x)
    return x


# i = int(input("Enter a number to check inverse: "))
z = [int(x) for x in input("Enter list (seporate with spaces): ").split()]
mod = int(input("Enter o(n) or mod (if multiple vaules of Z): "))

# print(inverse(i, mod))
print(gcd_working(z, mod))
# print("--------------------------")

