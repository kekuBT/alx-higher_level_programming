#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = []
    for i in matrix:
        tmpList = list(map(lambda x: x * x, i))
        matrix.append(tmpList)
    return (matrix)
