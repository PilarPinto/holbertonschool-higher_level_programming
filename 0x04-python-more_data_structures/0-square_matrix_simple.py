#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tmp_matrix = []
    for i in (matrix):
        tmp_matrix.append(list(map(lambda x: x ** 2, i)))
    return (tmp_matrix)
