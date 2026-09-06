# How many dictionary entries exist?
# What does counts.get(token, 0) return on the first "red"?
# What does it return on the third "red"?
print("=================== 1: Counting repeated keys ===================")
counts: dict[str, int] = {}

for token in ["red", "blue", "red", "green", "red"]:
    counts[token] = counts.get(token, 0) + 1

print(counts)

print()

# Does the dictionary contain three scores?
# What operation would be needed to preserve all three values?
print("=================== 2: Assignment to an existing key ===================")
scores: dict[str, float] = {}

scores["u1"] = 0.5
scores["u1"] = 0.8
scores["u1"] = 1.0

print(scores)

print()

# Is 0.0 missing?
# Is 0.0 a valid possible score?
# Why can truthiness be dangerous for validation?
print("=================== 3: Zero and truthiness ===================")
record = {"score": 0.0}

print(record["score"] is None)
print(bool(record["score"]))

if not record["score"]:
    print("ignored")
else:
    print("included")

print()

# Can .get() alone distinguish the two dictionaries?
# Which operation distinguishes them?
print("=================== 4: Missing key versus present None ===================")
first: dict[str, object] = {}
second: dict[str, object] = {"score": None}

print(first.get("score"))
print(second.get("score"))
print("score" in first)
print("score" in second)

print()

# Should a model score of True be accepted as the numeric value 1.0?
# How could you reject booleans while still accepting integers?
print("=================== 5: Boolean numbers ===================")
print(isinstance(True, bool))
print(isinstance(True, int))
print(float(True))
print(True + 2)

print()

# Which line fails?
# What exception do you expect?
# Why are some objects valid dictionary keys while others are not?
print("=================== 6: Hashable keys ===================")
result: dict[object, str] = {}

result["model-a"] = "ready"
result[("model", 1)] = "ready"
result[[1, 2]] = "ready"

print(result)

print()


