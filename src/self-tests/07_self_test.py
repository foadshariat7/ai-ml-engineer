# Which names are parameters?
# Which values are arguments?
# What is returned?
print("=================== 1: Parameter versus argument ===================")
def multiply(value, factor):
    return value * factor


result = multiply(5, 3)

print(result)

# Do both calls work?
# Why can keyword arguments appear in the opposite order?
# Would describe(0.9, "alice") mean the same thing?
print("=================== 2: Positional versus keyword ===================")
def describe(name, score):
    print(name, score)


describe("alice", 0.9)
describe(score=0.9, name="alice")

# Predict all outputs.
print("=================== 3: Default arguments ===================")
def power(value, exponent=2):
    return value ** exponent


print(power(3))
print(power(3, 3))
print(power(value=4))

# Predict exactly.
# Explain which calls share the same list.
print("=================== 4: Mutable default ===================")
def add(value, values=[]):
    values.append(value)
    return values


print(add(1))
print(add(2))
print(add(3, []))
print(add(4))

# Does the caller's list become [99]?
# Why?
print("=================== 5: Local rebinding ===================")
def replace(values):
    values = [99]


data = [1, 2, 3]

replace(data)

print(data)

# Why is this different from exercise 5?
print("=================== 6: Mutation ===================")
def update(values):
    values.append(99)


data = [1, 2, 3]

update(data)

print(data)

# Predict both outputs conceptually.
print("=================== 7: *args ===================")
def inspect(*values):
    print(values)
    print(type(values))


inspect(10, 20, 30)

# Which call fails?
# Why?
print("=================== 8: Keyword-only argument ===================")
def predict(text, *, temperature=0.7):
    return text, temperature


print(predict("hello", temperature=0.2))
# print(predict("hello", 0.2))

# What type is options?
# What dictionary does it contain?
print("=================== 9: **kwargs ===================")
def show(**options):
    print(options)


show(
    device="cuda",
    batch_size=32,
)

# Predict every printed line.
print("=================== 10: return versus print ===================")
def first():
    print(10)


def second():
    return 10


a = first()
b = second()

print(a)
print(b)

# Predict both results.
print("=================== 11: Function objects ===================")
def square(value):
    return value * value


operation = square

print(operation(5))
print(operation is square)

# Why don't we call double when passing it?
# Notice: double vs double()
print("=================== 12: Higher-order function ===================")
def apply(value, operation):
    return operation(value)


def double(value):
    return value * 2


print(apply(10, double))

# Where does factor come from after make_multiplier() has returned?
print("=================== 13: Closure ===================")
def make_multiplier(factor):
    def multiply(value):
        return value * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

# Predict the output.
# Identify:
# - base case;
# - recursive case.
print("=================== 14: Recursion ===================")
def countdown(value):
    if value == 0:
        return

    print(value)
    countdown(value - 1)


countdown(3)
