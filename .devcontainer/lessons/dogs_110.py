"""More practice with recursive functions."""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    if int(scores[idx]["score"]) < thresh:
        return False
    elif int(scores[idx]["score"]) >= thresh:
        if idx == len(scores) - 1:
            # print(f"Good dog, {scores[idx]["name"]}!")
            return True
        else:
            # print(f"Good dog, {scores[idx]["name"]}!")
            return all_good(scores, thresh, idx + 1)

    return False


pack: list[dict[str, str]] = [
    {"name": "Buster", "score": "10"},
    {"name": "Abby", "score": "9"},
    {"name": "Jack", "score": "6"},
    {"name": "Trooper", "score": "9"},
]

print(all_good(pack, 7, 0))
print(all_good(pack, 5, 0))
