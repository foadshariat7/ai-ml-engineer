def show(label, value):
    print(f"{label}: value={value}, id={id(value)}, type={type(value).__name__}")

# print("Example 1: two names, one list")
# a = [1, 2]
# b = a

# show("a before", a)
# show("b before", b)

# b.append(3)

# show("a after", a)
# show("b after", b)

# print("\nExample 2: rebinding")
# x = [10, 20]
# show("x original", x)

# x = ["new", "list"]
# show("x rebound", x)

# print("\nExample 3: dangerous default argument")

# def add_sample_bad(sample, samples=[]):
#     samples.append(sample)
#     return samples

# print(add_sample_bad("first"))
# print(add_sample_bad("second"))

# print("\nExample 4: safe default argument")

# def add_sample_good(sample, samples=None):
#     if samples is None:
#         samples = []
#     samples.append(sample)
#     return samples

# print(add_sample_good("first"))
# print(add_sample_good("second"))

# print("Example 5: Mutable and Immutable objects")
# experiment = (
#     "experiment-1",
#     ["accuracy", "precision"],
# )

# # experiment[0] = "experiment-2"

# experiment[1].append("recall")

# print(experiment)

# print("Example 6: Rebinding")
# a = [1, 2]
# b = a

# # b.append(3)
# b = b + [3]

# show("a after", a)
# show("b after", b)

# print("Example 7: Equality and Identity (is, ==)")
# a = [1, 2]
# b = a

# # show("a after", a)
# # show("b after", b)
# print(a is b)
# print(a == b)

# b = [1, 2]

# # show("a after", a)
# # show("b after", b)
# print("After:")
# print(a is b)
# print(a == b)

# x = "Foad"
# y = "Foad2"

# print(x is y)
# print(x == y)

# x = None

# print(x is None)

print("Example 8: Assignment, Shallow copy and Deep copy")
from copy import deepcopy

original = [
    ["sample-1", "sample-2"],
    ["sample-3"],
]
# alias = original
# print(alias is original)
# print(alias[0] is original[0])

# shallow = original.copy() # or copy.copy(original)
# print(shallow is original)
# print(shallow[0] is original[0])
# original[0].append("xyz")
# print(shallow)

deep = deepcopy(original)
print(deep is original)
print(deep[0] is original[0])
original[0].append("xyz")
print(deep)