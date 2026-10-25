# 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# def report(name, *scores, precision=2, **metadata):
#     print(type(scores).__name__)
#     print(type(metadata).__name__)
#     print(name, scores, precision, metadata)

# # 1
# test_dict = {
#     "device": "cuda",
#     "model": "small-transformer",
# }

# test_list = [0.91, 0.93, 0.95]

# report(
#     "experiment-1",
#     *test_list,
#     precision=3,
#     **test_dict,
# )

# 2
# report(
#     "experiment-1",
#     0.91,
#     0.93,
#     0.95,
#     precision=4,
#     device="cuda",
#     model="small-transformer",
# )

# 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# return multiple values
# def min_max(
#     values: list[int],
# ) -> tuple[int, int]:
#     return min(values), max(values)

# values = [2 ,3 ,4 ,5]

# # # Unpacking return values
# minimum, maximum = min_max(values)

# print(f"Minimum equals to {minimum} and Maximum equals to {maximum}")

# 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# Assign names to functions
def square(value):
    return value * value

# operation = square

# print(operation(5))

# 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# Function object versus function call
# square vs square()
# operations = [
#     square,
#     abs,
# ]

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


operations = {
    "add": add,
    "multiply": multiply,
}

print(operations["multiply"](3, 4))
# 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# Higher-Order Functions
# A higher-order function is a function that:
# - accepts another function as an argument
# - returns a function
# - or both

# def square(value):
#     return value * value

# def apply_to_all(
#     values,
#     transform,
# ):
#     return [
#         transform(value)
#         for value in values
#     ]

# print(apply_to_all([2,3,4], square))

# AI/ML apllication
    # loss functions
    # activation functions
    # metrics
    # callbacks
    # preprocessing functions
    # tokenizers
    # sampling functions
    # schedulers

# train(
#     model=model,
#     loss_fn=cross_entropy,
# )

# 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# Closure
# def make_multiplier(factor):
#     def multiply(value):
#         return value * factor

#     return multiply

# double = make_multiplier(2)
# triple = make_multiplier(3)
# quadruple = make_multiplier(4)
# print(double(10))
# print(triple(10))
# print(quadruple(10))

# # A closure doesn't necessarily copy the value
# def outer():
#     x = 10

#     def inner():
#         return x

#     x = 50
#     return inner

# f = outer()
# print(f())

# # Classic closure trap with loops (late binding)
# functions = []

# for i in range(3):
#     def f():
#         return i

#     functions.append(f)

# print(functions[0]())
# print(functions[1]())
# print(functions[2]())

# # ex:
# buttons = ["Start", "Stop", "Reset"]
# callbacks = []

# # trap
# for button in buttons:
#     def on_click():
#         print(f"{button} clicked")

#     callbacks.append(on_click)
    
# # fix
# callbacks = []

# for button in buttons:
#     def on_click(button=button):
#         print(f"{button} clicked")

#     callbacks.append(on_click)

# print(callbacks[0]())
# # expect: Start clicked
# # output: Reset clicked

# print(callbacks[1]())
# # expect: Stop clicked
# # output: Reset clicked

# print(callbacks[2]())
# # expect: Reset clicked
# # output: Reset clicked

# 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# Stateful closures

# def make_counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment

# counter = make_counter()

# print(counter())
# print(counter())
# print(counter())

# Class Equivalent
# class Counter:
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count += 1
#         return self.count

# counter = Counter()

# print(counter.increment())
# print(counter.increment())
# print(counter.increment())


# def make_storage():
#     items = []

#     def add(item):
#         # not needed nonlocal beacuse we do not rebinde
#         # items.append(item)
        
#         # needs nonlocal because we are rebinding
#         # nonlocal items
#         # items = items + [item]
        
#         return items

#     return add

# storage1 = make_storage()
# print(storage1("qqq"))
# print(storage1("qqq"))
# print(storage1("qqq"))
# print(storage1("qqq"))

# Real-world example: running total
# def make_accumulator():
#     total = 0

#     def add(amount):
#         nonlocal total
#         total += amount
#         return total

#     return add

# balance = make_accumulator()

# print(balance(100))
# print(balance(50))
# print(balance(-20))

# Another important example: training metrics
# def make_loss_tracker():
#     total_loss = 0.0
#     count = 0

#     def update(loss):
#         nonlocal total_loss, count

#         total_loss += loss
#         count += 1

#         return total_loss / count

#     return update

# track_loss = make_loss_tracker()

# print(track_loss(0.8))
# print(track_loss(0.6))
# print(track_loss(0.4))

# 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# Lambda
# Lambda is useful when a small function is needed briefly, for complex functions use def

# lambda PARAMETER=DEFAULT_VALUE : RETURN_EXPRESSION

# lambda x: x * x

# def square(x):
#     return x * x

# square = lambda x: x * x
# print(square(5))

# records = [
#     {"name": "a", "score": 0.7},
#     {"name": "b", "score": 0.9},
#     {"name": "c", "score": 0.8},
#     {"name": "d", "score": 0.6},
# ]

# print(sorted(records, key=lambda record: record["score"]))

# Late binding
# functions = []

# # without default value
# for value in range(3):
#     functions.append(
#         lambda: value
#     )

# # with default value
# for value in range(3):
#     functions.append(
#         lambda value=value: value
#     )

# print([function() for function in functions])

# 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# Recursion
# Recursion occurs when a function calls itself, directly or indirectly
# when to use:
    # trees
    # filesystem hierarchies
    # nested expressions
    # graph/search problems
    # divide-and-conquer algorithms

# Base case:
#   When should recursion stop?
# Recursive case:
#   How does the problem move toward the base case?

# def countdown(value):
#     if value == 0:
#         return

#     print(value)

#     countdown(value - 1)

# print(countdown(10))

# def factorial(n):
#     if n == 0:
#         return 1

#     return n * factorial(n - 1)

# print(factorial(5))

# 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# Performance & Memory
# Function calls have overhead
# A function call requires Python to:
    # - bind arguments;
    # - establish execution state;
    # - execute the body;
    # - return.

