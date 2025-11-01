def max_number(numbers: list[int]) -> int:
    current_max = numbers[0]
    for num in numbers:
        if current_max < num:
            current_max = num
    return current_max


def main():
    arr = [89, 23, 100, 434, 12]
    print(f"Max number of array: {arr} is {max_number(arr)}")


if __name__ == "__main__":
    main()
