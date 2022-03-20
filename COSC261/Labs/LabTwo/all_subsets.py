def all_subsets(s):
    subsets = []
    for i in range(2 ** len(s)):
        curr = []
        for j in range(len(s)):
            if (i >> j) % 2 == 1:
                curr.append(list(s)[j])
        subsets.append(curr)
    return [set(i) for i in subsets]


print(sorted(map(sorted, all_subsets({0, 1, 2}))))
print(sorted(map(sorted, all_subsets({'a', 'b'}))))
print({1} in all_subsets({0, 1, 2}))
