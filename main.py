def reduce_cost_matrix(matrix):
    for i in range(len(matrix)):
        min_value = min(matrix[i])
        for j in range(len(matrix[i])):
            matrix[i][j] -= min_value
    for j in range(len(matrix[0])):
        min_value = min([matrix[i][j] for i in range(len(matrix))])
        for i in range(len(matrix)):
            matrix[i][j] -= min_value

    return matrix


mat = [
        [35, 36, 36, 25],
        [31, 31, 35, 23],
        [33, 35, 39, 26],
        [32, 38, 33, 24]
      ]

reduced_mat = reduce_cost_matrix(mat)
print(reduced_mat)
