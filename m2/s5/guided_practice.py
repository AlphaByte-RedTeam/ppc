# 1. frequency counter
from collections import Counter


def top_k(tokens, k=3):
    c = Counter(tokens)
    return c.most_common(k)


# Demo
tokens = ["a", "b", "a", "c", "b", "a", "d"]
print(top_k(tokens, 3))  # [('a',3), ('b',2), ('c',1)]


# 2. Deduplicate preserving order
def dedupe_preserve_order(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


# 3. Anagrams bucket: Given words, produce buckets using dict where key = sorted chars (see group_anagrams above).
from collections import defaultdict


def anagram_buckets(words):
    buckets = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))  # canonical form
        buckets[key].append(word)
    return list(buckets.values())


# Demo
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram_buckets(words))


# 4. Build mini HashMap
class SimpleHashMap:
    def __init__(self, capacity=8):
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _bucket_index(self, key):
        return hash(key) % len(self._buckets)

    def set(self, key, value):
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]

        # update if exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # insert new key
        bucket.append((key, value))
        self._size += 1

        # load factor > 0.75 ? resize
        if self._size / len(self._buckets) > 0.75:
            self._resize(len(self._buckets) * 2)

    def get(self, key, default=None):
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return default

    # ------------------------
    # REQUIRED TASKS (Completed)
    # ------------------------

    def delete(self, key):
        """Remove key from hash map. Return True if deleted, False if not found."""
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return True
        return False

    def __contains__(self, key):
        """Return True if key exists in map."""
        return self.get(key) is not None

    # ------------------------
    # Resizing
    # ------------------------

    def _resize(self, new_capacity):
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(new_capacity)]
        self._size = 0  # will re-add every element

        for bucket in old_buckets:
            for k, v in bucket:
                self.set(k, v)

    def __repr__(self):
        return f"SimpleHashMap(size={self._size}, buckets={self._buckets})"
