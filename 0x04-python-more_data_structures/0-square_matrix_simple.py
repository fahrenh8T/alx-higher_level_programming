#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tempo = []
    for m in matrix:
        tempo.append(list(map(lambda m: m ** 2, m)))
    return (tempo)
