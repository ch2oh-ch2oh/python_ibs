from typing import List


def find_in_different_registers(words: List[str]):
    count = {}
    hasDup = {}
    for word in words:
        w = word.lower()
        if w in count:
            hasDup[w] = word in count[w]
            count[w].append(word)
        else:
            hasDup[w] = False
            count[w] = [word]
    return list(filter(lambda x: not hasDup[x], hasDup.keys()))
