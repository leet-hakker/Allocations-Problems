def is_valid(matrix):
    return len(matrix) == len(matrix[0])


def pprint(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


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


def hungarian(matrix):
    reduced_mat = reduced_cost_matrix(matrix)
    

mat = [
        [12, 23, 15, 40],
        [14, 21, 17, 20],
        [13, 22, 20, 30],
        [14, 24, 13, 10]
      ]

reduced_mat = reduce_cost_matrix(mat)
pprint(reduced_mat)
