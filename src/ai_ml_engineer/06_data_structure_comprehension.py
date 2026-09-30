# Comprehension: Compact way to create a new collection from an existing iterable
# List comprehension: 
# [expression for item in iterable]
# numbers = [1, 2, 3, 4, 5]
# values = [1, 2, 2, 3, 3, 3, 4, 1, 5]

# unique = []
# for v in values:
#     if v not in unique:      # scans the whole `unique` list so far — O(n)
#         unique.append(v)


# Comprehension (with set):
# seen = set()
# unique = [
#     v 
#     for v in values 
#     if not (v in seen or seen.add(v))
# ]
# print(unique)

# ex1:
# names = ["foad", "rezvan", "koroush"]
# upper_names = [name.upper() for name in names]
# print(upper_names)

# ex2:
# temperatures = [0, 10, 20, 30]
# fahrenheit = [ 
#     temperature * 9 / 5 + 32 
#     for temperature in temperatures 
# ]
# print(fahrenheit)

# [expression for item in iterable if condition]
# numbers = [1, 2, 3, 4, 5, 6]
# squared_evens = [ 
#     number ** 2
#     for number in numbers 
#     if number % 2 == 0 
# ]
# print(squared_evens)

# if else
# ex1:
# numbers = [-2, -1, 0, 1, 2]
# labels = [ 
#     "positive" if number > 0 else "non-positive"
#     for number in numbers 
# ] 
# print(labels)
# ex2:
# coord_numbers = [-2, -1, 0, 1, 2]
# result = [
#     number 
#     if number > 0 else 0 
#     for number in coord_numbers 
# ]
# print(result)

# Flatten list
# matrix = [ 
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# flattened = [
#     number
#     for row in matrix
#     for number in row
# ] 
# print(flattened)

# Nested List Comprehensions
# pairs = [ 
#     (x, y)
#     for x in [1, 2] 
#     for y in ["a", "b"] 
# ]

# pairs = [] 
# for x in [1, 2]: 
#     for y in ["a", "b"]: 
#         pairs.append((x, y))

# print(pairs)

# Dictionary Comprehensions
# { 
#   key_expression: value_expression 
#   for item in iterable 
# }

# ex1:
# numbers = [1, 2, 3, 4] 
# squares = { 
#     number: number ** 2 
#     for number in numbers 
# } 
# print(squares)

# ex2:
# prices = { 
#     "LAPTOP": 1000, 
#     "MOUSE": 50, 
#     "KEYBOARD": 100 
# } 

# discounted = { 
#     product.lower(): price * 0.9 
#     for product, price in prices.items() 
# } 
# print(discounted)

# your code should be readable
# result = [
#     x * y
#     for x in range(10)
#     for y in range(10)
#     if x % 2 == 0
#     if y % 3 == 0
# ]


# Machine learning example:

# probabilities = {
#     "sample-1": 0.9,
#     "sample-2": None,
#     "sample-3": 0.0,
# }

# valid = {
#     sample: probability
#     for sample, probability in probabilities.items()
#     if probability is not None
# }

# print(valid)

# Connection to NLP
# tokens = [
#     "AI",
#     "",
#     "Python",
#     "ML",
# ]

# clean = [
#     token.lower()
#     for token in tokens
#     if token
# ]

# print(clean)

