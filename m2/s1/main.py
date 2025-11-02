def max_number(arr: list[int]) -> int:
    # pass
    current_max_number = 0
    for num in arr:
        if num > current_max_number:
            current_max_number = num
    return current_max_number


def min_number(arr: list[int]):
    # pass
    current_min_number = float("inf")
    for num in arr:
        if num < current_min_number:
            current_min_number = num
    return current_min_number


array = [89, 23, 100, 434, 12]
# max_num = max_number(array)
min_num = min_number(array)
# print(f"Maximum number from array is {max_num}")
print(f"Minimum number from array is {min_num}")
