def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = [num ** 2 for num in row]
        new_matrix.append(new_row)
    return new_matrix

# Test the function with the given example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

