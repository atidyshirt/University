# Basically just using this file as a calculator

# NOTE: QUESTION ONE
def check_gen(expression, z):
    gen = True
    for i in z:
        if i not in expression:
            gen = False
    return gen

z = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
g2 = [(x**2)%17 for x in range(0,20)]
g3 = [(x**3)%17 for x in range(0,20)]
print(g2)
print(g3)
print(check_gen(g2, z))
print(check_gen(g3, z))

# NOTE: QUESTION TWO
# num operations per second to break 64 bit encryption in a year (brute force)
est = 2**64 / 2**25
print(est)


