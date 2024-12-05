def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise ValueError("Matrices must have the same dimensions")

    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

matrix1 = [[1, 3], [1, 4]]
matrix2 = [[4, 1], [2, 2]]
result = add_matrices(matrix1, matrix2)
print(result)