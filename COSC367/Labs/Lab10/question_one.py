import math

def euclidean_distance(v1, v2):
    return math.sqrt(sum((i - j) ** 2 for i, j in zip(v1, v2)))

def majority_element(labels):
    return max(list(labels), key=labels.count)

print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))
print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
print(majority_element("ababc") in "ab")
