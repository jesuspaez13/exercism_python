def latest(scores):
    return scores[len(scores)-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    scores_sorted = sorted(scores,reverse = True)
    return scores_sorted[:3]
