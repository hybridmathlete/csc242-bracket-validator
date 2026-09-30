def average(scores):
    total = sum([s for s in scores])
    return {"avg": total / len(scores)}
