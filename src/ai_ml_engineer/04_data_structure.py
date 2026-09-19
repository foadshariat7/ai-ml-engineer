
# # 1 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# # List example
fruits = ["apple", "banana", "orange", "mango"]
# print(fruits[1])
# print(fruits[-1])
# fruits[5] = "pineapple" # IndexError

# list of lists
# matrix = [ [1, 2], [3, 4], [5, 6] ]

# print(len(fruits))
# last_index = len(fruits) - 1
# print(last_index)

# fruits.append("kiwi")
# fruits.extend(["watermelon", "peach"]) # adds multiple elements
# fruits.insert(1, "cherry")

# fruits.remove("banana")

# poped_element = fruits.pop() # removes the last element
# poped_element = fruits.pop(2) # removes the index
# print(poped_element)

# del fruits[1:3]
# print(fruits)

# # iterate with index
# for index, name in enumerate(fruits):
#     print(index, name)

# fruits.sort()
# print(fruits)

# # reversing
# fruits.reverse() # mutate version
# reversed_fruits = fruits[::-1] # non-mutate version
# print(fruits)
# print(reversed_fruits)

# An empty list is falsy:

# items = []

# if not items:
#     print("Empty")
# else:
#     print("not empty")


# # 2 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# # Tuple example
# model_key = ("sentiment-model", 3)

# # A: The outer collection should not change
# model_key[0] = "vision-model"
# model_key.append(4)
# model_key.pop()

# data = ([1, 2], "test")
# # data[0] = [5, 6]   # Error
# data[0].append(3)
# print(data)

# # B: Position has a defined meaning
# coordinates = (47.6, -122.3) # x, y
# rgb = (255, 128, 0) # red, green, blue
# person = ("Foad", 46)

# # C: The object should sometimes be usable as a dictionary key
# # Dictionary keys must be hashable
# models = {
#     ("sentiment-model", 3): "ready",
#     ("sentiment-model", 4): "training",
# }

# locations = {
#     (47.6, -122.3): "Seattle",
#     (40.7, -74.0): "New York",
# }

# locations[(47.6, -122.3)] = "Seattle1"
# print(locations)

# # Disctionary keys should be hashable, ex: lists are not hashable
# # TypeError: unhashable type: 'list'
# loc = {
#     ("model", [1, 2, 3]): 1
# }

# loc_2 = {
#     ("model", "loaded"): 1
# }
# print(loc_2)

# # 3 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# # Set example
# unique_users = {"u1", "u2", "u3"}

# # # A: Uniqueness
# numbers = {1, 2, 2, 3, 3, 3}
# print(numbers)

# # B: Deduplication
# # list
# #   ↓
# # set()
# #   ↓
# # duplicates removed
# users = [
#     "u1",
#     "u2",
#     "u1",
#     "u3",
#     "u2",
#     "u1",
# ]

# unique_users = set(users)
# print("Unique users: ", unique_users)

# # C: Fast membership checks 
# # O(1) uses hashing to find the value efficiently
# users = {"u1", "u2", "u3", "u100"}

# if "u100" in users:
#     print("Found")

# # O(n)
# users_list = ["u1", "u2", "u3", "u100"]

# if "u100" in users_list:
#     print("Found")
    
# # D: Sets are not positional collections
# question is, does this element present? not the position
# users = {"u1", "u2", "u3"}
# users[0] → "u2" in users

# # E: Adding element(s)
# users = {"u1", "u2"}
# users.add("u3")
# print(users)

# users.update(["u4", "u5", "u6"])
# print(users)

# # F: Removing elements
# # remove()  → I expect this value to exist
# # discard() → remove it if it exists
# users.remove("u100") # Raises KeyError if element doesn't exist
# users.discard("u100") # No error if element doesn't exist

# # G: Union
backend_users = {"u1", "u2", "u3"}
frontend_users = {"u3", "u4", "u5"}

# # # two approaches
# # all_users = backend_users | frontend_users
# all_users = backend_users.union(frontend_users)
# print("Union: ", all_users) # {"u1", "u2", "u3", "u4", "u5"}

# # H: Intersection
# # two approaches
# both = backend_users & frontend_users
# both = backend_users.intersection(frontend_users)
# print("Intersection: ", both) # {"u3"}

# # I: Difference
# # Order is important
# diff1 = backend_users - frontend_users
# diff2 = frontend_users - backend_users

# print("Diff backend_users - frontend_users: ", diff1)
# print("Diff frontend_users - backend_users: ", diff2)

# # J: Symmetric difference
# s_diff = frontend_users ^ backend_users
# print("Symmetric difference: ", s_diff)

# # K: Subsets
admins = {"Foad", "Rezvan"}
users = {"Foad", "Rezvan", "Bob", "Jack"}

# print("Is admin subset of users? ", admins.issubset(users))
# print("Is admin subset of users? ", admins <= users)

# # L: Superset
# print("Is users superset of admins? ", users.issuperset(admins))

# # M: Set elements must be hashable
# values = {
#     "hello",
#     [1, 2, 3]
# }

# invalid_set = {[1, 2, 3]}
# valid_set = {(1, 2, 3)}

# # N: Create new set
# # {} doesn't create empty set
# wrong_new_set = {} # not a set, it's dictionary
# print(type(wrong_new_set).__name__)

# new_set = set() # creates new set
# print(type(new_set).__name__)

# # O: Frozen sets
# # sets are mutable but frozen sets are immutable
# permissions = frozenset({"read", "write"})

# # Real example for AI/ML
# # Example 1:
# labels = [
#     "positive",
#     "negative",
#     "positive",
#     "neutral",
#     "positive",
#     "negative",
# ]

# classes = set(labels)
# print(classes)
# print(len(classes))

# # Example 2:
# allowed_statuses = {
#     "pending",
#     "running",
#     "complete",
#     "failed",
# }
# status = "running"

# if status in allowed_statuses:
#     print("Valid")

# # Better than:
# # if (
# #     status == "pending"
# #     or status == "running"
# #     or status == "complete"
# #     or status == "failed"
# # ):
# #     print("Valid")

# # 4 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 🟡 
# # Dictionary example
# # key → value pairs

# # Create new dictionary
# new_dict = {}
# # or
# new_dict = dict()
# # or with value
# new_dict = dict(
#     name="Foad",
#     age=46,
#     active=True
# )

# # KEY          VALUE
# # ─────        ─────
# # "u1"    →     0.8
# # "u2"    →     0.4
scores_by_user = {
    "u1": 0.8,
    "u2": 0.4,
}
# print(scores_by_user["u1"])

# # A: Access a key → .get() versus []
# print(scores_by_user["u3"]) # KeyError: 'u3'
# print(scores_by_user.get("u3")) # prints None

# # We can also have default value
# print(scores_by_user.get("u3", 0)) # prints 0

# B: Add a new entry
# Notice the type hint
# user_admins: dict[str, str | int] = {
#     "name": "Foad",
# }

# user_admins["age"] = 46

# print(user_admins)

# C: keys should be hashable
# various_keys = {
#     "name": "Foad",       # str
#     10: "ten",            # int
#     3.14: "pi",           # float
#     True: "yes",          # bool
#     (1, 2): "point"       # tuple
# }

# # invalid keys:
# # list
# # dict
# # set
# # tuple with mutable object:
    # ("model", 1, 2, 3)
    #         ✅ hashable

    # ("model", (1, 2, 3))
    #         ✅ hashable

    # ("model", [1, 2, 3])
    #         ❌ not hashable

# D: Update a value
# various_keys["name"] = "Shariat"
# print(various_keys)

# E: Update multiple
# person = {
#     "name": "Foad",
#     "age": 46
# }

# person.update({
#     "age": 47,
#     "city": "Everett"
# })

# print(person)

# F: Remove item del, pop(), popitem()
person = {
    "name": "Foad",
    "age": 46,
    "city": "Everett"
}

# del person["age"]
# del person["email"] # raises KeyError

# age = person.pop("age")
# print(age)
# print(person)

# email = person.pop("email", None) # if no key, the default prevents KeyError

# item = person.popitem() # pops the last item in the dictionary

# print(item)
# print(person)

# Keep in mind dictionary changes size during iteration
# data = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }
# Risky and wrong
# for key in data:
#     if data[key] < 3:
#         del data[key]
        
# Internally, a dictionary is a hash table
# When you add or delete keys, 
# Python may need to change internal bookkeeping associated with that hash table

# print(list(data))

# Better with snapshot
# for key in list(data):
#     if data[key] < 3:
#         del data[key]
# print(data)

# print(data.items())
# print(type(data.items()).__name__)

# # Best with comprehension
# data = {
#     key: value
#     # unpacking
#     for key, value in data.items()
#     if value >= 3
# }
# print(data)

# # G: Clear the dictionary
# person.clear()
# print(person)

# # del vs clear()
# person.clear() # keeps the dictionary {}
# del person # removes the name binding
# print(person)

# # Check if key exists
# print("email" in person)

# Check if value exists
# print("Foad" in person.values())
# for value in person.values():
#     print(value)

# Return all keys
# print(person.keys())

# 2 ways to get the keys
# for key in person.keys():
#     print(key)

# for item in person:
#     print(item)
    

# # H: Get all the items
# person = {
#     "name": "Foad",
#     "age": 46
# }
# print(person.items())

# # Genrates tuples - Extremely useful 
# for item in person.items():
#     print(item)

# # Unpacking
# for key, value in person.items():
#     print(key, value)

# I: setdefault()
# Creates key if not exists with a default value
students = [
    ("Foad", "Python"),
    ("Koroush", "Java"),
    ("Rezvan", "Python")
]

groups = {}

for name, language in students:
    groups.setdefault(language, []).append(name)

print(groups)

