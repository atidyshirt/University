def cycle_length(start, count=0):
    if start == 1:
        return count + 1
    elif start % 2 == 0:
        return cycle_length((start / 2), count+1)
    else:
        return cycle_length((3 * start + 1), count+1)
def recursive_divide(x, y):
    if x - y == 0:
        return 1
    elif x - y < 0:
        return 0
    else:
        return 1 + recursive_divide(x-y, y)
def my_enumerate(items, counter=0):
    if len(items) < 1:
        return []
    else:
        tup = (counter, items[0])
        items.pop(0)
        return [tup] + my_enumerate(items, counter+1)
def num_rushes(slope, rush, slide):
    if slope <= 0:
        return 1
    else:
        slope = slope - rush
        if slope <= 0:
            return 1
        else:
            slope = slope + slide
            return 1 + num_rushes(slope, rush*0.95, slide)
def dumbo_func(data, i=0):
    """Takes a list of numbers and does weird stuff with it"""
    if i >= len(data):
        return 0
    else:
        c = dumbo_func(data, i + 1)
        if (data[i] // 100) % 3 != 0:
            c += 1
        return c
def all_pairs(lista, listb):
    if len(lista) == 0 or len(listb) == 0:
        return []
    else:
        return [(lista[0], listb[0])] + all_pairs(lista[1:], listb) + all_pairs(lista, listb[1:])
