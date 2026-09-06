print("=================== 1: Aliasing ===================")
x = ["train"]
y = x

y.append("validation")

print(x)
print(y)
print(x is y)

print()

print("=================== 2: Rebinding ===================")
x = ["train"]
y = x

y = y + ["validation"]

print(x)
print(y)
print(x is y)

print()

print("=================== 3: Mutable default ===================")
def record_score(
    score: float,
    scores: list[float] = [],
) -> list[float]:
    scores.append(score)
    return scores


print(record_score(0.8))
print(record_score(0.7))
print(record_score(0.6, []))
print(record_score(0.5))

print()

print("=================== 4: Equality and Identity ===================")
left = [1, 2, 3]
right = [1, 2, 3]
alias = left

print(left == right)
print(left is right)
print(left == alias)
print(left is alias)

print()

print("=================== 5: Mutation followed by rebinding ===================")
def transform(values: list[int]) -> list[int]:
    values.append(3)
    values = [99]
    return values


data = [1, 2]
result = transform(data)

print(data)
print(result)

print()
