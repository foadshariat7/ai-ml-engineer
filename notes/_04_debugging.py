# Diagnostic debugging task
# Identify at least eight separate defects or missing behaviors

def average_scores(
    records: list[dict[str, object]],
) -> dict[str, float]:
    res = dict[str, float]

    for obj in records:
        name = obj.user_id
        score = obj.score
        res[name] = score

    return res