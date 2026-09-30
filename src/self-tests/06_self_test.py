# What is printed?
# How many output values are created?
# Does this change values?
print("=================== 1: Basic transformation ===================")
values = [1, 2, 3, 4]

result = [
    value * 2
    for value in values
]

print(result)

# Is zero included?
# Does every input value produce an output?
# Is value > 0 a transformation or a filter?
print("=================== 2: Filtering ===================")
values = [-3, -2, -1, 0, 1, 2, 3]

result = [
    value
    for value in values
    if value > 0
]

print(result)

# Does Python square the negative numbers and then discard them?
# Or does the condition determine which items reach the expression?
# Predict the exact list.
print("=================== 3: Transformation + filtering ===================")
values = [-3, -2, -1, 0, 1, 2, 3]

result = [
    value * value
    for value in values
    if value > 0
]

print(result)

# Why are the lengths different?
# Which expression removes elements?
# Which expression transforms every element?
print("=================== 4: Filter versus conditional expression ===================")
values = [-2, 0, 3]

a = [
    value
    for value in values
    if value > 0
]

b = [
    value if value > 0 else 0
    for value in values
]

print(a)
print(b)

# How many unique lengths exist?
# Why can the result contain fewer entries than the input?
# Is a set comprehension guaranteed to preserve the original order?
print("=================== 5: Set comprehension ===================")
words = [
    "AI",
    "ML",
    "AI",
    "Python",
    "ML",
]

result = {
    len(word)
    for word in words
}

print(result)

# What are the keys?
# What are the values?
# Which part of the comprehension appears before the colon?
print("=================== 6: Dictionary comprehension ===================")
names = ["Foad", "Rezvan", "Alice"]

result = {
    name: len(name)
    for name in names
}

print(result)

# Is "alice" present?
# Is "bob" present?
# Why?
# Does if score mean the same thing as if score is not None?
print("=================== 7: The truthiness trap ===================")
scores = {
    "alice": 0.0,
    "bob": None,
    "charlie": 0.7,
}

valid = {
    user: score
    for user, score in scores.items()
    if score
}

print(valid)




