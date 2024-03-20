def square_matrix_map(matrix=[]):
    newList = list(map(lambda l: list(map(lambda i: i**2, l)), matrix))
    return (newList)
