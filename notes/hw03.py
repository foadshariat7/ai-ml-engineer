"""Homework 03: Variables, types, scope, and control flow.

This is a script, not a set of functions to implement. Each exercise's
instructions are the comment block directly above its `print(...)`
header; write your code between that header and the next one.
"""

# Create variables for:
#   - your name
#   - your age
#   - your current lesson number
#   - whether you have completed the lesson
#   - an optional value that currently has no value
#
# Print each of the five variables above along with its type:
#   value
#   type(value)
print("=" * 25, "Exercise 1: Variables and types", "=" * 25)


# Rebind `value` (given below) to, in order:
#   - a float
#   - a string
#   - a Boolean
#   - None
#
# After every one of those four assignments, print:
#   value
#   type(value)
#   id(value)
print("=" * 25, "Exercise 2: Rebinding and identity", "=" * 25)

value = 100


# Without executing this file first, predict every line of output below.
# Then:
#   1. Remove the local `x` (inside `inner`). Predict the new output again.
#   2. Also remove the enclosing `x` (inside `outer`). Predict again.
print("=" * 25, "Exercise 3: Scope (predict, then verify)", "=" * 25)

x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

print("global:", x)


# Determine and print whether `number` (given below) is:
#   - positive / negative / zero
#   - even / odd
#   - divisible by 3
#   - divisible by 5
#   - between 10 and 20 (inclusive)
print("=" * 25, "Exercise 4: Number properties", "=" * 25)

number = 17


# Determine and print, for `text` (given below):
#   - the first character
#   - the last character
#   - the first 10 characters
#   - the string reversed
#   - the length
#   - the uppercase version
#   - the lowercase version
#   - whether "Intel" occurs in the string
#
# Hint for reversing a string: text[::-1]
print("=" * 25, "Exercise 5: String analyzer", "=" * 25)

text = "Artificial Intelligence"


# For every number from 1 through 100, print:
#   - "Fizz" if it is divisible by 3
#   - "Buzz" if it is divisible by 5
#   - "FizzBuzz" if it is divisible by both 3 and 5
#   - the number itself otherwise
print("=" * 25, "Exercise 6: FizzBuzz", "=" * 25)
