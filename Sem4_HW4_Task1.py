def transpose_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    if num_rows == 0 or num_cols == 0:
        return []

    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


original_matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = transpose_matrix(original_matrix)
print(transposed_matrix)
