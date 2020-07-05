# similar to using a two constructors in java
def cycle_length(n, count=0):
    count += 1
    if n == 1:
        return count
    elif n % 2 == 0:
        return cycle_length(n/2, count)
    else:
        return cycle_length(n*3 + 1, count)

#  print(cycle_length(22))

def recursive_divide(x, y, count = 0):
    if x < y:
        return count
    elif x == 0:
        return 0
    else:
        count += 1
        return recursive_divide(x - y, y, count)

#  print(recursive_divide(8, 3))

def my_enumerate(items, index=0):
    if index < len(items):
        return [(index, items[index])] + my_enumerate(items, (index + 1))
    else:
        return []

#  print(my_enumerate([10,20,30]))
#  ans = my_enumerate(['dog', 'pig', 'cow'])
#  print(ans)

def num_rushes(height, height_gain, back_slide, counter=0):
    counter += 1
    if height_gain >= height:
        return counter
    else:
        return num_rushes(height - height_gain + back_slide, height_gain * 0.95, back_slide * 0.95, counter)

#  ans = num_rushes(10, 10, 9)
#  print(ans)

#  ans = num_rushes(100, 10, 0)
#  print(ans)

#  ans = num_rushes(100, 15, 7)
#  print(ans)

#------------------------------------------------------------------ Not Complete (Q6 L2)

import sys
sys.setrecursionlimit(100000)

def dumbo_func(data):
    """Takes a list of numbers and does weird stuff with it"""
    if len(data) == 0:
        return 0
    elif (data[0] // 100) % 3 != 0:
        return 1 + dumbo_func(data[1:])
    else:
        return dumbo_func(data[1:])

data = [677, 90, 785, 875, 7, 90393, 10707]
# print(dumbo_func(data))

#------------------------------------------------------------------ Not Complete (Q7 L2)



def all_pairs(list1, list2, i = 0):
    if i >= len(list1):
        return []
    return all_pairs_2(list1[i], list2) + all_pairs(list1, list2, i + 1)

def all_pairs_2(number, list2, i = 0):
    if i >= len(list2):
        return []
    return [(number, list2[i])] + all_pairs_2(number, list2, i + 1)




# print(all_pairs([1, 2], [10, 20, 30]))

#------------------------------------------------------------------ END


def perms(items):
    result = []
    if len(items) == 0:
        return [()]
    if len(items) == 1:
        return [tuple(items)]
    for item in items:
        items_remaining = [
            i for i in items
                if i != item
            ]
        sets_of_perms = perms(items_remaining)
        for perm in sets_of_perms:
            result.append(tuple([item]) + tuple(perm))
    return result

print(perms([1,2,3]))
#------------------------------------------------------------------ END

def combinations(items, r):
    if r > len(items):
        return []
    if r == 0:
        return [()]
    return combinations2(items, r)

def combinations2(items, n, sets=None):
    if sets == None:
        sets = []
    if len(items) == n:
        if sets.count(tuple(items)) == 0:
            sets.append(tuple(items))
        return sets
    
    for i in range(len(items)):
        remaining = items[:i] + items[i+1:]
        combos = combinations2(remaining, n, sets)
    return combos

ans = []
for combo in combinations([1, 2, 3, 4], 3):
    ans.append(tuple(sorted(combo)))
print(sorted(ans))

#------------------------------------------------------------------ END



#------------------------------------------------------------------ END



#------------------------------------------------------------------ END



