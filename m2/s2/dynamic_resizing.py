import sys
lst = []
for i in range(10):
    lst.append(i)
    print(f"Length: {len(lst)}, Size in bytes: {sys.getsizeof(lst)}")

