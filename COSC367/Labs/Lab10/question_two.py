import math

def euclidean_distance(v1, v2):
    return math.sqrt(sum((i - j) ** 2 for i, j in zip(v1, v2)))

def majority_element(labels):
    return max(list(labels), key=labels.count)

def knn_predict(input, examples, distance, combine, k):
    neighbours = sorted(((distance(input, ex[0]), ex[1]) for ex in examples), key=lambda x: x[0])
    selected, neighbours = neighbours[:k], neighbours[k:]
    for unselected in neighbours:
        if unselected[0] == selected[-1][0]: selected.append(unselected)
    return combine([i[1] for i in selected])

examples = [
    ([2], '-'),
    ([3], '-'),
    ([5], '+'),
    ([8], '+'),
    ([9], '+'),
]

distance = euclidean_distance
combine = majority_element

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print(x, knn_predict([x], examples, distance, combine, k))
    print()

