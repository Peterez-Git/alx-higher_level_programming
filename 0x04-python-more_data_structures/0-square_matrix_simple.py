#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        square = []
        for j in i:
            square.append(j ** 2)
        square_matrix.append(square)
    return square_matrix
