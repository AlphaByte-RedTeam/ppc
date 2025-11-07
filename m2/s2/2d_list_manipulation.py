matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[matrix[j][i] for j in range(3)] for i in range(3)]
print(transpose)  # [[1,4,7],[2,5,8],[3,6,9]]

