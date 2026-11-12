# # *** Most Important Python concept ***
# # Generators: produces values one at a time, "Lazy"
# # A normal list creates and stores all its values immediately
# def numbers():
#     count = 1
#     print("Starting")
#     print("Starting")
#     print("Starting")
#     print("Starting")
#     print("Starting")
#     print("Starting")
#     yield count
#     count += 1
#     yield count
#     print("Middle")
#     count += 1
#     yield count
#     count += 1
#     yield count
#     print("Ending")
#     count += 1
#     yield count
# result = numbers()
# print(result)
# print(next(result))
# print(next(result))
# print(next(result))

# List vs generator
# list_numbers = list(range(1_000_000))
# print(list_numbers)

# Lazy evaluation
# def numbers():
#     for number in range(1_000_000):
#         yield number

# gen = numbers()
# print(gen)
# print(next(gen))

# Creation comparison
# list_numbers = [x * 2 for x in range(5)]
# gen_numbers = (x * 2 for x in range(5))

# print("Numbers in a list: ", list_numbers)
# print("Numbers in generator: ", gen_numbers)

# def squares(n):
#     for number in range(n):
#         yield number ** 2

# gen = squares(5)
# A generator is both: Iterable, Iterator

# Iterable: Something you can loop over
# Iterator: Something that remembers iteration state and supports next()
# next(gen)
# for value in gen:
#     print(value)

# Important: 
# *** A generator can usually only be consumed once, It does not automatically restart ***
# *** A generator doesn't contain a normal indexed collection ***

# Be careful
# gen = (x for x in range(10))

# print(5 in gen)
# print(5 in gen)
# print(list(gen)) # converts to list and consumes generator

# Practical Example 1:
# List version:
# def create_batches(items, batch_size):
#     batches = []

#     for i in range(0, len(items), batch_size):
#         batches.append(items[i:i + batch_size])

#     return batches

# items = [1, 2, 3, 4, 5, 6]

# print(create_batches(items, 2))

# Generator version:
# def create_batches(items, batch_size):
#     for i in range(0, len(items), batch_size):
#         yield items[i:i + batch_size]

# batches = create_batches([1, 2, 3, 4, 5, 6], 2)
# print(next(batches))
# print(next(batches))
# print(next(batches))

# Practical Example 2:
# def load_users():
#     yield {
#         "user_id": "alice",
#         "score": 90,
#     }

#     yield {
#         "user_id": "bob",
#         "score": 80,
#     }

#     yield {
#         "user_id": "charlie",
#         "score": 95,
#     }

# records = load_users()
# for record in records:
#     print(record)
    
# yield from
# numbers = (x for x in range(5))
# numbers = [x for x in range(5)]
# def combined():
#     yield 'a'
#     yield from numbers
#     yield 'b'

# gen = combined()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# for el in gen:
#     print(el)

# Extremly helpful example:
# data engineering
# machine learning
# file processing
# API streams
# database processing
# ETL pipelines
# large datasets
# PyTorch Dataset
# DataLoader
# batching
# token datasets
# LLM training
# numbers = range(1_000_000)
# evens = (x for x in numbers if x % 2 == 0)
# squares = (x ** 2 for x in evens)
# large = (x for x in squares if x > 100)

# print(next(large))
# print(next(large))




