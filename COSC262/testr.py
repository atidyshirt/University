def perms(items):
    if len(items) == 0:
        return [()]
    if len(items) == 1:
        return [tuple(items)]
    sets = []
    for item in items:
        left = [i for i in items if i != item]
        permus = perms(left)
        for perm in permus:
            sets.append(tuple([item]) + tuple(perm))
    return sets

for perm in sorted(perms([1, 2, 3])):
    print(perm)