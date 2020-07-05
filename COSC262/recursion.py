def backwards(data):
    if len(data) == 0:
        return ""
    else:
        return data[-1] + backwards(data[:-1])

#  print(backwards("Hi there!"))

def odds(data):
    if len(data) == 0:
        return []
    elif data[0] % 2 == 0:
        return odds(data[1:])
    else:
        return [data[0]] + odds(data[1:])

#  print(odds([0, 1, 12, 13, 14, 9, -11, -20]))

def squares(data):
    if len(data) == 0:
        return []
    else:
        return [int(data[0])**2] + squares(data[1:])

#  print(squares([1, 13, 9, -11]))

def findInc(data, target):
    if len(data) == 0:
        return 0
    if data[0] == target:
        return 0
    else:
        return 1 + findInc(data[1:], target)

def find(data, val):
    x = findInc(data, val)
    if x >= len(data):
        return -1
    return x

#  print(findInc(["hi", "there", "you", "there"], "there"))
#  print(find([10, 20, 30], 0))

def sort_of(num):
    res = []
    if len(num) == 0:
        return res
    #go back through list
    res = [num[-1]]
    for i in range(len(num) - 2, -1, -1):
        if num[i] <= res[-1]:
            res.append(num[i])
        else:
            res.append(res[-1])
    return list(reversed(res))

print(sort_of([1, 2, 3, 3]))
print(sort_of(list(range(10**5))))

