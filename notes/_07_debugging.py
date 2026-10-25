"""Debugging 07: Functions.

Each part below contains a deliberate bug. Read the code, answer the
questions in the comments, then compare with `_07_debugging.md`.

Do not fix the code in this file — the bugs are the exercise. Running the
file as-is fails at Part B (and Part C would fail too).
"""


# ---------------------------------------------------------------------------
# Part A — Mutable default
# ---------------------------------------------------------------------------
# A test passes alone but fails after another test calls the function.
#
# Explain:
#   1. the root cause;
#   2. when the list is created;
#   3. why test ordering reveals the bug;
#   4. a safe fix.

def record_loss(
    loss,
    history=[],
):
    history.append(loss)
    return history


# ---------------------------------------------------------------------------
# Part B — Missing return
# ---------------------------------------------------------------------------
# Diagnose exactly what happens.

def normalize(value):
    result = value / 100
    print(result)


score = normalize(50)
print(score * 2)


# ---------------------------------------------------------------------------
# Part C — Callback accidentally called
# ---------------------------------------------------------------------------
# Explain:
#   1. why this fails;
#   2. the difference between `double` and `double()`;
#   3. the correct call.

def apply(value, operation):
    return operation(value)


def double(value):
    return value * 2


result = apply(
    5,
    double(),
)


# ---------------------------------------------------------------------------
# Part D — Closure late binding
# ---------------------------------------------------------------------------
# Predict the result, explain why, then fix it.

operations = []

for factor in [2, 3, 4]:
    operations.append(
        lambda value: value * factor
    )

print(
    [
        operation(10)
        for operation in operations
    ]
)


# ---------------------------------------------------------------------------
# Part E — Recursive failure
# ---------------------------------------------------------------------------
# Explain:
#   - the missing base case;
#   - what eventually happens;
#   - why multiplying by decreasing numbers does not automatically
#     terminate recursion.

def factorial(value):
    return value * factorial(value - 1)
