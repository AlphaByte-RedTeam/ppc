a = [[1, 2], [3, 4]]
b = a.copy()  # shallow copy
b[0][0] = 99
print(a)  # [[99, 2], [3, 4]]  -> changed!

mem_address_a = id(a)
mem_address_b = id(b)
print(f"Memory address of a: {hex(mem_address_a)}")
print(f"Memory address of b: {hex(mem_address_b)}")
