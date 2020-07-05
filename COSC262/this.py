def things(list1, list2, index1=0, n=0):
    if index1 <= len(list1):
        if n <= len(list2):
            if list2[n] > list1[index1]:
                return [(list1[index1], list2[n])] + things(list1, list2, index1, n+1)
        else:
            if list2[n] > list1[index1]:
                return [(list1[index1], list2[n])] + things(list1, list2, index1+1, n)

print(things([1,2,3,4], [1,3,45,3]))