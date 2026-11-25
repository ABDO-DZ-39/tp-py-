import math
# Euclidean Distance
def euclidean_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

print(euclidean_distance([1, 2], [4, 6]))
 #Manhattan Distance
def manhattan_distance(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))

print(manhattan_distance([1, 2], [4, 6]))
#Cosine Similarity
import math

def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))

    norm_a = math.sqrt(sum(x ** 2 for x in a))
    norm_b = math.sqrt(sum(y ** 2 for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot_product / (norm_a * norm_b)

print(cosine_similarity([1, 2], [4, 6]))