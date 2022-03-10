def all_strings(alpha, length):
    if length == 0:
        return ['']
    prev = all_strings(alpha, length - 1)
    tmp = []
    for i in prev:
        for j in alpha:
            tmp.append(str(i) + str(j))
    return tmp

print(sorted(all_strings({0, 1}, 3)))
print(sorted(all_strings({'a', 'b'}, 2)))
print(len(all_strings({'a', 'b', 'c'}, 2)))
