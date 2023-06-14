#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''function computes the square value of all integers of a matrix'''
    tempo = []
    for m in matrix:
        tempo.append(list(map(lambda m: m ** 2, m)))
    return (tempo)
