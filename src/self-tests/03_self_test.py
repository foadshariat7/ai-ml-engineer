# What does this print?
print("=================== 1: Scope ===================")
x = 10

def show():
    x = 20
    print(x)

show()
print(x)

print()

# Which part of LEGB finds x?
print("=================== 2: LEGB (Local, Enclosing, Global, Built-in) ===================")
x = "global"

def outer():
    x = "enclosing"

    def inner():
        print(x)

    inner()

outer()

print()

# What is wrong with this code?
print("=================== 3: Built-in shadowing ===================")
list = [1, 2, 3]
# numbers = list("123")

print()

# Explain the difference between the three operators.
print("=================== 4: Integer division ===================")
print(7 / 2)
print(7 // 2)
print(7 % 2)

print()

# Is it: 64 or: 512 Why?
print("=================== 5: Exponentiation ===================")
result = 2 ** 3 ** 2
print(result)

print()

# What does this print?
print("=================== 6: String indexing ===================")
language = "Python"

print(language[0])
print(language[-1])
print(language[1:4])

print()

# Will this work? If not, why not?
print("=================== 7: String immutability ===================")
name = "Foad"
# name[0] = "T"

print()

# Does and always return a Boolean?
print("=================== 8: and ===================")
result = "" and "Python"

print(result)

print()

# what's the output
print("=================== 9: or ===================")
name = ""

display_name = name or "Anonymous"

print(display_name)

print()

# Write the equivalent expression using and
print("=================== 10: Chained comparisons ===================")
# 0 <= score <= 100

# What is printed? Is there a problem with the condition order?
print("=================== 11: Condition order ===================")
score = 95

if score >= 60:
    print("Passed")
elif score >= 90:
    print("Excellent")
else:
    print("Failed")

print()

# What are the outputs?
print("=================== 12: Loops (for, break, continue, while, else) ===================")
# 1
for i in range(2, 8, 2):
    print(i)

#2
for number in range(10):
    if number == 3:
        break

    print(number)

#3
for number in range(5):
    if number == 2:
        continue

    print(number)

# #4
# count = 0

# while count < 5:
#     print(count)

#5
for number in range(3):
    print(number)
else:
    print("Done")
