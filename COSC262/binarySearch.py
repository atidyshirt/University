###############################################################

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <=end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            # this will pull out if we find the value we want
            return midpoint
        elif item < midpoint_value:
            # if item is lower than guess, redefine topmost to index below
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1

    return None

sequence_a = [1,2,3,4,5,6,7,8,9,14,23]
item_a = 14

print(binary_search(sequence_a, item_a))

###############################################################

#  BINARY SEARCH COMPLEXITY

#  search size of n elements
#  when going through search each comparison 1/2's results

#  n = len(sequence)
#  k = num steps

#  n * 1/2 * 1/2 * ... * 1/2 = n/2^k
#  therefore               k = log2(n)

# BIG O
# BEST CASE:    O(1)
# WORST CASE:   O(log n)
# AVERAGE:      O(log n)

###############################################################
