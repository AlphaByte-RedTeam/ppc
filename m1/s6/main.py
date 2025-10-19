def main():
    # guided practices answers:
    # 1. Shopping List
    print("Guided Practice 1.")
    #   a. Create a list of 5 groceries.
    groceries: list[str] = [
        "apple",
        "banana",
        "milk",
        "flour",
        "baking soda",
    ]
    #   b. Print the list and its length.
    print(f"List of groceries is {groceries}")
    print(f"The length of the groceries is {len(groceries)}")

    print("\n------------------\n")
    # 2. Append & Remove
    print("Guided Practice 2.")
    #   a. Add an item "egg" to your list.
    groceries.append("egg")
    #   b. Remove one existing item.
    groceries.remove("banana")
    #   c. Print the updated list.
    print(f"Updated list of groceries is {groceries}")

    print("\n------------------\n")
    # 3. Sum of Numbers
    print("Guided Practice 3.")
    #   a. Given a list [5, 10, 15, 20], use a loop to compute the total.
    numbers = [5, 10, 15, 20]
    #   b. Print the total.
    total = 0
    for number in numbers:
        total += number
    print(f"The total of the numbers is {total}")

    print("\n------------------\n")
    # 4. 2D Access
    print("Guided Practice 4.")
    #   a. Create a 2D list [[1,2,3],[4,5,6],[7,8,9]].
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #   b. Print the middle element.
    print(f"The middle element of the matrix is {matrix[1][1]}")

    print("\n------------------\n")
    # 5. Simple Dictionary
    print("Guided Practice 5.")
    #   a. Create a dictionary for a student:
    student = {"name": "John", "age": 20, "grade": "A"}
    #   b. Print each key and value using a loop.
    for key, value in student.items():
        print(f"{key}: {value}")

    print("\n------------------\n")
    # 6. Nested Data Access
    print("Guided Practice 6.")
    #   a. Create a dictionary with list values:
    #      classroom = {"students": ["Ari", "Bima", "Cici"]}
    classroom = {"students": ["Ari", "Bima", "Cici"]}
    #   c. Print the second student’s name.
    print(f"The second student's name is {classroom['students'][1]}")


if __name__ == "__main__":
    main()
