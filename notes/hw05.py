"""Big O practice: analyze each function before running it."""

# For each function:
# write the time complexity;
# write the auxiliary space complexity;
# explain why in a comment;
# only then run the code.

sample_numbers = [10, 20, 30, 40, 50]


# Function 1 🟡
def get_last(numbers):
    return numbers[-1]

# Time:
# Space:
# Why:


# Function 2 🟡
def contains(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False

# Time (best case):
# Time (worst case):
# Space:
# Why:


# Function 3 🟡
def combinations(numbers):
    for x in numbers:
        for y in numbers:
            print(x, y)

# Time:
# Space:
# Why:


# Function 4 🟡
def double_values(numbers):
    return [number * 2 for number in numbers]

# Time:
# Space:
# Why:


# Function 5 🟡
def unique_values(numbers):
    return set(numbers)

# Time:
# Space:
# Why:


# Function 6 🟡
def sorted_values(numbers):
    return sorted(numbers)

# Time:
# Space:
# Why:


# Challenge 🟡 Rewrite find_pairs
def find_pairs(numbers, target):
    result = []

    for x in numbers:
        for y in numbers:
            if x + y == target:
                result.append((x, y))

    return result

# This is O(n²).
# Design a version using a set or dictionary that avoids checking every
# possible pair. Replace the `...` with your implementation.
# Target average time: O(n)


def find_pairs_fast(numbers, target):
    ...

# Time:
# Space:
# Why:


# Run only after you have written your answers:
# print(get_last(sample_numbers))
# print(contains(sample_numbers, 30))
# combinations(sample_numbers)
# print(double_values(sample_numbers))
# print(unique_values(sample_numbers))
# print(sorted_values(sample_numbers))
# print(find_pairs(sample_numbers, 50))
# print(find_pairs_fast(sample_numbers, 50))


# Complexity questions:
# What does (n) represent in each function?
# Which functions return a new collection, and what does that cost in space?
# Which function has a different best case and worst case, and why?
# Is a list comprehension a different complexity class than the equivalent loop?
# Why is set(numbers) not O(1), even though a single lookup is O(1) on average?
# Why is sorted(numbers) not O(n), even though it is written on one line?
# Which of these functions mutate their input?
# In find_pairs, what makes the cost n² rather than 2n?
# What does the set version trade away to buy its speed?
