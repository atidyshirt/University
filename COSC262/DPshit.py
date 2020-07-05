def lcs(u, v):
    """
    Main LCS Method:
    sets list c and then runs inner method
    """
    c = [[-1]*(len(v) + 1) for _ in range(len(u) + 1)]
    lcs_helper(u, v, c, 0, 0)
    def inner_lcs(c, i, j, result=""):
        """
        Inner LCS:
        takes values and puts them into a string called 'result'
        responsilble for printing the actual vaues
        """
        if i == len(u) or j == len(v):
            return result
        else:
            if u[i] == v[j]:
                result = result + u[i]
                return inner_lcs(c, i + 1, j + 1, result)
            elif c[i][j + 1] > c[i + 1][j]:
                return inner_lcs(c, i, j + 1, result)
            else:
                return inner_lcs(c, i + 1, j, result)
    return inner_lcs(c, 0, 0)
 
 
def lcs_helper(u, v, c, i, j):
    """
    LCS Helper:
    responsible for initiating dynamic programming
    """
    if c[i][j] >= 0:
        return c[i][j]
 
    if i == len(u) or j == len(v):
        q = 0
    else:
        if u[i] == v[j]:
            q = 1 + lcs_helper(u, v, c, i + 1, j + 1)
        else:
            q = max(lcs_helper(u, v, c, i + 1, j),
                    lcs_helper(u, v, c, i, j + 1))
    c[i][j] = q
    return q