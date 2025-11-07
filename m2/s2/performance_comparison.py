import time
from array import array

nums_list = list(range(1_000_000))
nums_array = array("i", range(1_000_000))

start = time.time()
sum(nums_list)
print("List sum:", time.time() - start)

start = time.time()
sum(nums_array)
print("Array sum:", time.time() - start)
