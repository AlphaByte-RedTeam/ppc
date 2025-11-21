def counter(words):
    counts = {}
    for f in words:
        try:
            counts[f] += 1
        except KeyError:
            counts[f] = 1
    return counts


words = ["fuck", "banana", "apple", "orange", "banana", "apple"]
print(counter(words))
