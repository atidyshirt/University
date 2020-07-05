#  print(min(12, 25))
#  print(max(12, 25))

a = 2
b = 200000
list_=[1,400,3,4,20,6,28,8,65,23]
listb=[2,4,6]

#  if a < min(a, b):
    #  print("A")
#  else:
    #  print("B")

#  if a*b >= max(a, b):
    #  print("E")
#  else:
    #  print("F")

def my_max(a):
    return sorted(a)[-1]
#  print(my_max(list_))

def shorter(a):
    b = a[1:]
    print(b)
#  shorter(list_)

def deviations(a):
    devs = []
    n = len(a)
    for x in a:
        mean = sum(a) / n
        dev = x - mean
        devs.append(dev)
    return devs

#  print(deviations(listb))

def almost_all_test(lista):
    result = []
    totalList = sum(lista)
    for item in lista:
        result.append(totalList - (item))
    return result

#  print(almost_all_test([1,2,3]))
#  print(almost_all_test(list(range(10**5))))

def sort_of(numbers): 
    result = [] 
    for i in range(len(numbers)): 
        sub = sorted(numbers[i:])
        print(sub)
        result.append(sub[0]) 
    return result

print(sort_of(list_))
