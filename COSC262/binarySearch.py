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
