# Predict the complexity first.

# How many operations run here?
# Does the size of items change that number?
# What is the time complexity?
print("=================== 1: Constant time ===================")
def first(items):
    return items[0]


print()

# How many times does the loop body run?
# If items gets twice as long, how much more work is done?
print("=================== 2: A single loop ===================")
def print_all(items):
    for item in items:
        print(item)


print()

# How many times does the inner loop run for each outer iteration?
# How many pairs are printed in total?
print("=================== 3: Nested loops ===================")
def pairs(items):
    for x in items:
        for y in items:
            print(x, y)


print()

# Is this O(n²) because there are two loops?
# Are the loops nested or sequential?
# What happens to constant factors in Big-O?
# Think carefully.
print("=================== 4: Two sequential loops ===================")
def two_loops(items):
    for item in items:
        print(item)

    for item in items:
        print(item)


print()

# How many times can n be halved before the loop stops?
# If n is 1024, how many iterations run?
# Which complexity class does repeated halving produce?
print("=================== 5: Repeated halving ===================")
def halve(n):
    while n > 1:
        n //= 2


print()

# What are:
# best case?
# worst case?
# Where is target in each of those cases?
# Which case does Big-O usually describe?
print("=================== 6: Linear search ===================")
def find(items, target):
    for item in items:
        if item == target:
            return True

    return False


print()
