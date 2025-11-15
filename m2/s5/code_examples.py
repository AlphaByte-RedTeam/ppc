# 1. Frequency word counter
def word_count(text: str):
    counts = {}
    for token in text.split():
        counts[token] = counts.get(token, 0) + 1
    return counts


# Usage
txt = "foo bar foo baz foo bar"
print(word_count(txt))  # {'foo': 3, 'bar': 2, 'baz': 1}


# 2. Detect Duplicates (set)
def has_duplicates(seq):
    seen = set()
    for x in seq:
        if x in seen:
            return True
        seen.add(x)
    return False


ex_seq = "foo bar foo baz foo bar"
print(has_duplicates(ex_seq.split()))  # True

# 3. Group Anagrams (dict + sorted key)
from collections import defaultdict  # IMPORTANT!! Module import should be at the top


def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


# Example
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat','tea','ate'], ['tan','nat'], ['bat']]

# 4. Set Operations (union/intersection/diff)
a = {1, 2, 3}
b = {2, 3, 4}
print("union:", a | b)
print("intersection:", a & b)
print("difference (a-b):", a - b)


# 5. Simple HashMap (separate chaining)
class SimpleHashMap:
    def __init__(self, capacity=8):
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _bucket_index(self, key):
        return hash(key) % len(self._buckets)

    def set(self, key, value):
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size / len(self._buckets) > 0.75:
            self._resize(len(self._buckets) * 2)

    def get(self, key, default=None):
        idx = self._bucket_index(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        return default

    def _resize(self, new_capacity):
        old = self._buckets
        self._buckets = [[] for _ in range(new_capacity)]
        self._size = 0
        for bucket in old:
            for k, v in bucket:
                self.set(k, v)
