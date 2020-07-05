######################################

def LinearSearch(sequence, item):
    for i in range (len(sequence)):
        if sequence[i] == item:
            return i
    return None

list_a = [1,2,3,4,5,6,7,8,9,10,21]
item_a = 10

print(LinearSearch(list_a, item_a))

######################################

#  LINEAR SEARCH COMPLEXITY

#  BEST CASE:  O(1)
#  WORST CASE: O(n)
#  AVERAGE:    O(n)

######################################
