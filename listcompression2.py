matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


odd_diagonal_elements = [matrix[i][i] for i in range(len(matrix)) if matrix[i][i] % 2 != 0]


print(odd_diagonal_elements)
