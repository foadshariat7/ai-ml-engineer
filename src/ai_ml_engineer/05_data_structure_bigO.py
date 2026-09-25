# # Big O — code examples
# # The full explanation lives in 05_data_structure_bigO.md


# # 1 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Big O fundamentals

# # C: What does n mean?
# def print_names(names):
#     for name in names:
#         print(name)

# names = ["Ali", "Sara"]   # n = 2


# # 2 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Reading complexity from loops

# # A: O(1) — constant time
# def get_first(items):
#     return items[0]

# x = numbers[5]          # list indexing      → O(1)
# person["name"]          # dictionary lookup  → O(1) average
# "value" in my_set       # set membership     → O(1) average

# # B: O(n) — linear time
# def print_all(items):
#     for item in items:
#         print(item)

# # C: Multiple sequential operations → O(n), not O(n²)
# def process(items):
#     for item in items:
#         print(item)

#     for item in items:
#         print(item)

# # D: Nested loops → n × n = n² → O(n²)
# for x in items:
#     for y in items:
#         print(x, y)

# # E: Sequential loops add; nested loops multiply
# # sequential ≈ n + n → O(n)
# for x in items:
#     ...

# for y in items:
#     ...

# # nested ≈ n × n → O(n²)
# for x in items:
#     for y in items:
#         ...

# # F: Independent input sizes → O(n + m)
# def process(users, products):
#     for user in users:
#         print(user)

#     for product in products:
#         print(product)

# # nested independent inputs → O(n × m)
# for user in users:
#     for product in products:
#         print(user, product)


# # 3 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Simplification rules

# # C: Complexity is not determined by the number of code lines
# x = data[0]
# y = data[1]
# z = data[2]
# # three operations, still O(1)

# for item in data:
#     do_something(item)
# # two lines, but O(n)


# # 4 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Common complexity classes

# # D: O(n log n) — Python's built-in sorting
# numbers.sort()
# sorted(numbers)

# # E: O(n²) — quadratic time
# def all_pairs(numbers):
#     for x in numbers:
#         for y in numbers:
#             print(x, y)

# # F: Triangular loops are still O(n²)
# for i in range(n):
#     for j in range(i, n):
#         print(i, j)

# # G: O(2ⁿ) — exponential time
# def fibonacci(n):
#     if n <= 1:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)


# # 5 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Best case, average case, worst case
# def find(numbers, target):
#     for number in numbers:
#         if number == target:
#             return True

#     return False

# numbers = [7, 4, 20, 99, 42]

# find(numbers, 7)    # first element   → best case  O(1)
# find(numbers, 42)   # last element    → worst case O(n)
# find(numbers, 100)  # not in the list → worst case O(n)


# # 6 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Time complexity vs space complexity

# # time O(n), extra space O(n)
# def duplicate(numbers):
#     result = []

#     for number in numbers:
#         result.append(number)

#     return result

# # time O(n), extra space O(1)
# def print_numbers(numbers):
#     for number in numbers:
#         print(number)


# # 7 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Python list complexity
# numbers = [10, 20, 30, 40]

# numbers[2]            # A: index access        → O(1)
# numbers[2] = 100      # B: assignment by index → O(1)
# 30 in numbers         # C: search              → O(n)
# numbers.index(30)     # D: index()             → O(n)
# numbers.append(50)    # E: append              → amortized O(1)
# numbers.pop()         # F: pop from end        → O(1)
# numbers.insert(0, 5)  # G: insert at beginning → O(n), elements shift right
# numbers.pop(0)        # H: remove from start   → O(n), elements shift left


# # 8 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Dictionary complexity
# user = {
#     "name": "Foad",
#     "age": 46,
# }

# user["name"]              # lookup     → O(1) average
# user["city"] = "Seattle"  # insertion  → O(1) average
# del user["age"]           # deletion   → O(1) average
# "name" in user            # membership → O(1) average


# # 9 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Set complexity
# ids = {10, 20, 30, 40}
# 30 in ids        # O(1) average

# ids = [10, 20, 30, 40]
# 30 in ids        # O(n)


# # 10 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # A very important optimization example
# users = [...]
# blocked_users = [...]

# # both are lists of roughly n elements → O(n²)
# for user in users:
#     if user in blocked_users:
#         print("blocked")

# # convert to a set → O(n)
# blocked_users = set(blocked_users)

# for user in users:
#     if user in blocked_users:
#         print("blocked")


# # 11 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Better grouping algorithm

# # A: Grouping into lists — the duplicate check is list membership
# result = {}

# for word in words:
#     length = len(word)

#     if length not in result:
#         result[length] = []

#     if word not in result[length]:   # list membership → O(m) per bucket
#         result[length].append(word)

# # B: Grouping into sets → O(n) average
# result = {}

# for word in words:
#     length = len(word)

#     if length not in result:
#         result[length] = set()

#     result[length].add(word)

# # C: Convert back to lists if lists are required
# result = {
#     length: list(group)
#     for length, group in result.items()
# }


# # 12 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Hidden costs in everyday operations

# # A: String complexity — strings are immutable
# text = text + "a"        # copies n characters → O(n)

# result = ""

# for character in characters:
#     result += character  # copies a growing string → total ≈ O(n²)

# result = "".join(characters)   # ≈ O(n)

# # B: Sorting complexity — one line is not O(1)
# numbers.sort()           # O(n log n)
# sorted(numbers)          # O(n log n)

# for number in sorted(numbers):   # O(n log n) + O(n) → O(n log n)
#     print(number)

# # C: Function calls can hide complexity
# def process(numbers):
#     for number in numbers:       # O(n)
#         if number in numbers:    # O(n) — list membership, not O(1)
#             print(number)
# # → O(n × n) = O(n²)

# # D: len() in Python
# len(numbers)             # O(1) — the length is stored internally

# for _ in range(len(numbers)):
#     ...

# # E: Slicing
# subset = numbers[2:8]    # k selected elements → time O(k), space O(k)

# while numbers:
#     numbers = numbers[1:]   # copies most of the list each pass → O(n²)


# # 13 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Amortized complexity
# numbers.append(value)    # amortized O(1), not plain O(1)
# # a resize costs O(n), but resizing does not happen on every append


# # 14 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Reading loops carefully

# # A: Early exit does not automatically change Big O
# for number in numbers:
#     if number == target:
#         return True
# # worst case: target is last or absent → O(n)

# # B: Conditions inside loops
# for number in numbers:
#     if number % 2 == 0:  # constant-time work
#         print(number)
# # → O(n), an if does not add a factor of n

# # C: Loop that runs half of n
# for i in range(n // 2):
#     print(i)
# # ≈ n / 2 → O(n)

# # D: Loop that jumps by 2
# for i in range(0, n, 2):
#     print(i)
# # ≈ n / 2 → O(n)

# # E: Loop that doubles each time
# i = 1

# while i < n:
#     i *= 2
# 1, 2, 4, 8, 16, ... → ≈ log₂(n) steps → O(log n)

# # F: Loop that halves each time
# while n > 1:
#     n //= 2
# # → O(log n)

# # G: Nested loop with logarithmic inner loop
# for i in range(n):       # O(n)
#     j = 1

#     while j < n:         # O(log n)
#         j *= 2
# # → O(n log n)


# # 15 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Recursive complexity
# def countdown(n):
#     if n == 0:
#         return

#     countdown(n - 1)
# # ≈ n calls → time O(n), call-stack space O(n)


# # 16 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Big O and machine learning
# # Explanation only — see 05_data_structure_bigO.md
# # sequence length = n → the attention matrix is ≈ n × n → O(n²)


# # 17 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Complexity is not the same as performance
# # Explanation only — see 05_data_structure_bigO.md
# # Algorithm A: 1000n   Algorithm B: n²
# # For very small n, B may actually run faster.


# # 18 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Big O vs Big Ω vs Big Θ
# # O → upper bound, Ω → lower bound, Θ → tight bound
# for item in items:
#     print(item)
# # always visits every element → Θ(n), usually called O(n) in conversation


# # 19 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Practical Big O analysis method
# # Step 1: identify the inputs — what grows? (n = users, m = products)
# # Step 2: find the loops — single, nested?
# # Step 3: inspect the operations inside the loops
# x in numbers      # list   → O(n)
# x in lookup       # set    → O(1) average
# # Step 4: analyze function calls — sorted(data) is not constant time
# sorted(data)      # O(n log n)
# # Step 5: combine sequential sections by addition → O(n) + O(n²) = O(n²)
# # Step 6: combine nested work by multiplication  → O(n) × O(n) = O(n²)
# # Step 7: drop constants                         → O(5n) = O(n)
# # Step 8: drop dominated terms                   → O(n² + n + 1) = O(n²)


# # 20 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡
# # Worked examples

# # A: one indexed lookup → time O(1)
# def example_a(numbers):
#     print(numbers[0])

# # B: visits each element → time O(n), extra space O(1)
# def example_b(numbers):
#     total = 0

#     for number in numbers:
#         total += number

#     return total

# # C: builds a new list → time O(n), space O(n)
# def example_c(numbers):
#     result = []

#     for number in numbers:
#         result.append(number * 2)

#     return result

# # D: nested loops → time O(n²)
# def example_d(numbers):
#     for x in numbers:
#         for y in numbers:
#             print(x, y)

# # E: sequential loops → O(n + n) → O(n)
# def example_e(numbers):
#     for x in numbers:
#         print(x)

#     for x in numbers:
#         print(x)

# # F: sort O(n log n) + loop O(n) → O(n log n)
# def example_f(numbers):
#     numbers.sort()

#     for number in numbers:
#         print(number)

# # G: set build O(n) + loop O(n) × lookup O(1) → O(n)
# def example_g(numbers):
#     lookup = set(numbers)

#     for number in numbers:
#         if number in lookup:
#             print(number)


# Exercise 1 — Constant or linear?
# Analyze:
def mystery(numbers):
    return numbers[0] + numbers[-1]

# Exercise 2 — Find the hidden operation
def mystery(numbers):
    for number in numbers:
        if number in numbers:
            print(number)

# Do not answer based only on the visible loop.

# Exercise 3 — Lists vs sets
# Analyze:
def common(a, b):
    result = []

    for item in a:
        if item in b:
            result.append(item)

    return result

# Assume:
# len(a) = n
# len(b) = m

# Then redesign it using a set.
# Compare the complexities.

# Exercise 4 — Comprehension
# Analyze:

result = [
    x * 2
    for x in numbers
]

# Time?
# Space?

# Exercise 5 — Nested comprehension
result = [
    (x, y)
    for x in numbers
    for y in numbers
]

# Time?
# Space?

# Exercise 6 — Sorting

# Analyze:

def smallest(numbers):
    return sorted(numbers)[0]

# Could this be implemented with better asymptotic time complexity?
# Explain.

# Exercise 7 — String building
# Compare:
result = ""

for character in characters:
    result += character

# with:

result = "".join(characters)

# Explain why their behavior can differ substantially.

# 1- What does Big O measure?
# 2- Does O(n) mean an algorithm takes n seconds?
# 3- What does n normally represent?
# 4- Why is list indexing O(1)?
# 5- Why is searching a list O(n)?
# 6- Why is dictionary lookup usually O(1)?
# 7- Why do nested loops often produce O(n²)?
# 8- Why do two sequential loops usually remain O(n)?
# 9- What is the difference between:
# O(n + m)

# and:

# O(nm)
# 10- Why do we drop constants?
# 11- Simplify:
# O(5n + 200)
# 12- Simplify:
# O(n² + 50n + 1000)
# 13- What makes an algorithm O(log n)?
# 14- What is a common example of O(n log n)?
# 15- What is amortized complexity?
# 16- Why is list append amortized O(1)?
# 17- What is the difference between time and space complexity?
# 18 -Why can:
# x in some_list

# be expensive inside a loop?

# 19- How can converting a list to a set improve an algorithm?
# 20- Why can a one-line Python expression still have high complexity?
