def generators(n, z):
    s = set(z)
    results = []
    for a in s:
        g = set()
        for x in s:
            g.add((a**x) % n)
        if g == s:
            results.append(a)
    return results

print("cant express modulo")

z = [int(x) for x in input("Enter list (seporate with spaces): ").split()]
mod = int(input("Enter o(n) or mod (if multiple vaules of Z): "))


print(generators(mod, z))
