#!/usr/bin/python3
'''module: 101-lazy_matrix_mul
contains a function that multiplies two matrices
'''
import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    '''function: lazy_matrix_mul
    return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    '''
    return (npy.matmul(m_a, m_b))
