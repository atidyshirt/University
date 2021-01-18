def LCSubStr(X, Y, m, n):

    # Create a table to store lengths of
    # longest common suffixes of substrings.
    # Note that LCSuff[i][j] contains the
    # length of longest common suffix of
    # X[0...i-1] and Y[0...j-1]. The first
    # row and first column entries have no
    # logical meaning, they are used only
    # for simplicity of the program.

    # LCSuff is the table with zero
    # value initially in each cell
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

    # To store the length of
    # longest common substring
    result = 0

    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
            print("i=" + str(i) + " j=" + str(j) + " result=" + str(result))
    return result + 1

# Driver Program to test above function
X = 'them'
Y = 'tim'

m = len(X)
n = len(Y)

print('Length of Longest Common Substring is',
                      LCSubStr(X, Y, m, n))

def longestSubstringFinder(string1: str, string2: str):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer

print(longestSubstringFinder("gcagct", "cttgacgt"))

from difflib import SequenceMatcher

def longestSubstring(str1,str2):

     # initialize SequenceMatcher object with
     # input string
     seqMatch = SequenceMatcher(None,str1,str2)

     # find match of longest sub-string
     # output will be like Match(a=0, b=0, size=5)
     match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))

     # print longest substring
     if (match.size!=0):
          print (str1[match.a: match.a + match.size])
     else:
          print ('No longest common sub-string found')

# Driver program
if __name__ == "__main__":
    str1 = 'gcagct'
    str2 = 'cttgacgt'
    longestSubstring(str1,str2)

