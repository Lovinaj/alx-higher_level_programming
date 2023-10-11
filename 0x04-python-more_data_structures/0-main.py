#!/usr/bin/python3

square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

'''
#!/usr/bin/python3

# @matrix is a 2 dimensional array

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        alt_matrix = []
        for column in row:
            alt_matrix.append(column ** 2)
        new_matrix.append(alt_matrix)

    return (new_matrix)
'''
