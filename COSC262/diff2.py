def create_table(s1, s2): 
    """
    creates DP table
    """
    s1 = s1.splitlines()
    s2 = s2.splitlines()
    n_rows = len(s1) + 1
    n_cols = len(s2) + 1
    # Creates empty table with 3 * max_number_of_lines
    T = [n_cols * [0] for row in range(n_rows)]
     
    for i in range(n_rows):
        for j in range(n_cols):
            if i == 0: 
                T[i][j] = j
            elif j == 0:
                T[i][j] = i
            elif s1[i-1] == s2[j-1]: 
                T[i][j] = T[i-1][j-1]
            else: 
                T[i][j] = 1 + min(T[i-1][j], T[i][j-1], T[i-1][j-1]) 
    return T

def line_edits(s1, s2):
    """this is a docstring"""
    table = create_table(s1, s2)
    s1 = s1.splitlines()
    s2 = s2.splitlines()
    i = len(s1)
    j = len(s2)
    res = []
    while i > 0 or j > 0:
        if i == 0:
            res.append(('I', '', s2[j-1]))
            j -= 1
        elif j == 0:
            res.append(('D', s1[i-1], ''))
            i -= 1
        elif s1[i-1] == s2[j-1]:
            res.append(('C', s1[i-1], s2[j-1]))
            i -= 1
            j -= 1
        else:
            if table[i-1][j-1] <= table[i][j-1] and table[i-1][j-1] <= table[i-1][j]:
                subsequence = lcs(s1[i-1], s2[j-1])
                first = find(s1[i-1], subsequence)
                second = find(s2[j-1], subsequence)
                res.append(('S', first, second))
                i -= 1
                j -= 1
            elif table[i-1][j] <= table[i][j-1]:
                res.append(('D', s1[i-1], ''))
                i -= 1
            else:
                res.append(('I', '', s2[j-1]))
                j -= 1
    return res[::-1]

def find(str1, lcs1):
    """a"""
    return_str = ""
    index = 0
    for char in str1:
        if len(lcs1) > index and lcs1[index] == char:
            return_str += char
            index += 1
        else:
            return_str += "[[{}]]".format(char)
    return return_str

def lcs(s1, s2): 
    """
    Bottom Up Approach to the LCS problem:
    builds table of values "L", populastes it
    loops to find the LCS of two given strings
    """
    m = len(s1)
    n = len(s2) 
    L = [[0 for x in range(n+1)] for x in range(m+1)] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
    index = L[m][n] 
    res = [""] * (index+1) 
    res[index] = "" 
    i = m
    j = n 
    while i > 0 and j > 0: 
        if s1[i-1] == s2[j-1]: 
            res[index-1] = s1[i-1] 
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]: 
            i -= 1
        else: 
            j -= 1
    return ("".join(res))


print("------------T3-----------------")
print()
s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
print()
print("------------T3-----------------")
