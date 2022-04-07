def shuffle(s, t):
    if s == '' or t == '': # if they are empty, return the other one (appending makes a single clause)
        return list(s + t) 
    a = shuffle(s[1:], t)
    for i in range(0, len(a)):
        a[i] = s[0] + a[i]
    b = shuffle(t[1:], s)
    for i in range(0, len(b)):
        b[i] = t[0] + b[i]
    return list(set(a + b))


# print(sorted(shuffle('', 'e')))
# print()
# print(sorted(shuffle('ab', 'cd')))
# print(sorted(shuffle('abab', 'baba')))

print(sorted(shuffle('', 'e')))

# /1*|1*00|000*|00*11*

def shuffle_language(A, B):
    if len(A) == 0 and len(B) == 0: 
        return []
    result = []
    for a in A:
        for b in B:
            result += shuffle(a, b)    
    return list(set(result))

# print(sorted(shuffle_language({'ab'}, {'cd', 'e'})))
# print(sorted(shuffle_language({}, {'aa', 'ab', 'bb'})))
# print(sorted(shuffle_language({'aba', 'baa', 'aab'}, {'aab', 'bba', 'aaa'})))
