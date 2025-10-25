groceries = set(
    tuple(
        [
            "apple",
            "apple",
            "apple",
            "apple",
            "banana",
            "milk",
            "flour",
            "baking soda",
        ]
    )
)

# print(groceries[0])  # apple
# groceries[0] = "orange"  # modifying an array

# print(groceries[0])  # orange
print(groceries)
groceries.add("orange")
print(groceries)

# karakteristik list vs tuple
# list = mutable (artinya value bisa diubah)
# tuple = immutable (artinya value tidak bisa diubah)
#
# set = mutable (artinya value bisa diubah), set tidak berurutan
# frozenset = immutable (artinya value tidak bisa diubah)
