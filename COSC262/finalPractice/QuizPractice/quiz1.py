""" Code for quiz one - rest of quesitons done in book """
def almost_all(numbers): 
    "Sums numbers each time"
    return [sum(numbers) - x for x in numbers]
def almost_all_better(numbers, n=-1):
    "Only sums numbers once"
    if n == -1:
        n = sum(numbers)
    return [n - x for x in numbers] 
def sort_of(numbers): 
    result = [] 
    for i in range(len(numbers)): 
        sub = sorted(numbers[i:]) 
        result.append(sub[0]) 
    return result
def concat_list(list_of_strings, res = ""):
    if len(list_of_strings) == 0:
        return res
    else:
        res = res + list_of_strings[0]
        return concat_list(list_of_strings[1:], res)
def product(data, total=1):
    if len(data) == 0:
        return total
    else:
        total *= data[-1]
        return product(data[:-1], total)
def backwards(s):
    if len(s) <= 1:
        return s
    else:
        return backwards(s[1:]) + s[0]
def odds(nums):
    if len(nums) <= 0:
        return []
    elif nums[0] % 2 != 0:
        return [nums[0]] + odds(nums[1:])
    else:
        return odds(nums[1:])
def squares(nums):
    if len(nums) <= 0:
        return []
    else:
        return [(nums[0]**2)] + squares(nums[1:]) 
def find(data, value):
    if len(data) <= 0:
        return 1
    elif value == data[0]:
        return find(data[1:], value) + 1
    else:
        return find(data[1:], value)
