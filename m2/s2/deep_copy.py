import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 99
print(a)  # [[1, 2], [3, 4]]  -> safe

mem_add_a = id(a)
mem_add_b = id(b)
print(f"Memory address of a: {hex(mem_add_a)}")
print(f"Memory address of b: {hex(mem_add_b)}")
