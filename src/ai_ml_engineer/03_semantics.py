import math

# #1
# def calculate():
#     result = 100
# calculate()
# print(result)

# #2
# def calculate():
#     score = 95
#     print(score)
# calculate()

# def outer():
#     message = "Hello"
#     def inner():
#         print(message)
#     inner()
# outer() 

# #3
# message = "global"
# def outer():
#     def inner():
#         print(message)
#     inner()
# outer()

# #4
# list = [1, 2, 3]

# numbers = list("123")
# print(numbers)

# x = "global"

# def show():
#     x = "local"
#     print(x)

# show()
# print(x)

# #5
# count = 10
# def increment():
#     global count
#     count += 1
# increment()
# print(count) 

# #6
# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#     increment()
#     increment()
#     print(count)
# counter()

# #7
# print(0.1 + 0.2)
# x = 0.1 + 0.2
# print(x == 0.3)
# print(math.isclose(0.1 + 0.2, 0.3))

# +   # جمع
# -   # تفریق
# *   # ضرب
# /   # تقسیم معمولی
# //  # تقسیم صحیح
# %   # باقی‌مانده
# **  # توان
# print(7 / 2)
# print(7 // 2)
# print(7 % 2)
# print(7 ** 2)

# x = 45
# print(x % 2 == 0)


# #8
# x = int("42")
# y = int(3.14)
# z = int("Hello")

# print(x)
# print(y)
# print(z)

# #9
# message = """
# Hello
# Welcome to Python
# """

# print(message)

# #10
# user_name = "Foad Shariat"
# important_list = [7, 8, 9, 10, 11, 12, 13]
# # slice[start:stop]
# print(user_name[1:7])
# print(important_list[1:3])
# print(user_name[:7])
# print(important_list[:3])
# print(user_name[1:])
# print(important_list[2:])

# #11
# first = "Machine"
# second = "Learning"
# result = first + " " + second
# print(result)

# #12
# print("Foad" * 3)

# #13
# text = "  Python Programming  "

# print("Strip the text: ", text.strip())
# print("Convert text to lower case: ", text.lower())
# print("Convert text to upper case: ", text.upper())
# print("Replace text: ", text.replace("Python", "AI"))
# print("Text starts with Python: ", text.startswith("Python"))
# print("Text starts with Python: ", text.strip().startswith("Python"))
# print("Python,AI,ML".split(","))

# #14
# name = "Foad"
# score = 95

# message = f"{name} scored {score}"
# print(message)

# #15
# language = "Python"
# name_list = ["Foad", "Shariat", "Python"]
# print("Py" in language)
# print("Java" not in language)
# print("Foad" in name_list)

# #16
# score = 95
# if 0 <= score <= 100:
# # if score >= 0 and score <= 100:
#     print("Valid score")

# #17
# score = 87
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# else:
#     grade = "F"
# print(grade)

# #18
# age = 20
# status = "Adult" if age >= 18 else "Minor"
# print(status)

# # if age >= 18:
# #     status = "Adult"
# # else:
# #     status = "Minor"

# print("Status: ", status)

#range(start, stop, step)
# #19
# for number in range(0, 10, 2):
#      print(number)

# #20
# count = 0
# while count <= 5:
#     print(count)
#     count += 1

# 1- break 2- continue 3- pass
# #21
# for number in range(10):
#     if number == 5:
#         break
#     print(number)

# #22
# for number in range(5):
#     if number == 2:
#         continue
#     print(number)

# for number in range(5):
#     pass

# numbers = [1, 3, 7, 9]

# for num in numbers:
#     if num % 2 == 0:
#         print(f"Found an even number: {num}")
#         break
# else:
#     print("No even numbers were found in the list.")

# #23
# username = "Foad"
# scores = [88, 95, 72, 100]

# total = 0

# for score in scores:
#     if not 0 <= score <= 100:
#         print(f"Invalid score: {score}")
#         continue

#     total += score

# average = total / len(scores)

# if average >= 90:
#     grade = "Excellent"
# elif average >= 80:
#     grade = "Good"
# elif average >= 70:
#     grade = "Passing"
# else:
#     grade = "Needs improvement"

# print(f"{username}'s average: {average:.2f}")
# print(f"Result: {grade}")

