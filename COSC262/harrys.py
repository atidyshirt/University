while i > 0 or j > 0:
        if i == 0:
            lst.append(('I', '', lst2[j-1]))
            j -= 1
        elif j == 0:
            lst.append(('D', lst1[i-1], ''))
            i -= 1
        elif lst1[i-1] == lst2[j-1]:
            lst.append(('C', lst1[i-1], lst2[j-1]))
            i -= 1
            j -= 1
        else:
            if table[i-1][j-1] <= table[i][j-1] and table[i-1][j-1] <= table[i-1][j]:
                lst.append(('S', lst1[i-1], lst2[j-1]))
                i -= 1
                j -= 1
            elif table[i-1][j] <= table[i][j-1]:
                lst.append(('D', lst1[i-1], ''))
                i -= 1
            else:
                lst.append(('I', '', lst2[j-1]))
                j -= 1