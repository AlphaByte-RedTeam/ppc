from collections import Counter


def top_k(tokens, k=3):
    c = Counter(tokens)
    return c.most_common(k)


tokens = ["a", "b", "a", "c", "b", "a", "d"]
print(top_k(tokens, 3))


def dedupe_preserve_order(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


from collections import defaultdict


def anagram_buckets(words):
    buckets = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        buckets[key].append(word)
    return list(buckets.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram_buckets(words))


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
        bucket = self._buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return default

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

    def _resize(self, new_capacity):
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(new_capacity)]
        self._size = 0

        for bucket in old_buckets:
            for k, v in bucket:
                self.set(k, v)

    def __repr__(self):
        return f"SimpleHashMap(size={self._size}, buckets={self._buckets})"


hash_map = SimpleHashMap()
hash_map.set("a", 1)
hash_map.set("b", 2)
print(hash_map.get("a"))
print(hash_map.get("b"))
print(hash_map.delete("b"))
print("b" in hash_map)
