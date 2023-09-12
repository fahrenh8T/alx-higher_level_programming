#!/usr/bin/python3
'''module: 9-queens
solves the N-queens puzzle.
determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.
'''

import sys


def init_board(n):
    '''method: init_board
    initialize an `n`x`n` sized chessboard with 0's'''
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    '''method: board_deepcopy
    return a deepcopy of a chessboard
    '''
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    '''method: get_solution
    returns the list of lists representation of a solved chessboard
    '''
    solution = []
    for r in range(len(board)):
        for w in range(len(board)):
            if board[r][w] == "Q":
                solution.append([r, w])
                break
    return (solution)


def xout(board, row, col):
    '''method: xout
    X out spots on a chessboard.
    all spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    '''
    for w in range(col + 1, len(board)):
        board[row][w] = "x"
    for w in range(col - 1, -1, -1):
        board[row][w] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    w = col + 1
    for r in range(row + 1, len(board)):
        if w >= len(board):
            break
        board[r][w] = "x"
        w += 1
    w = col - 1
    for r in range(row - 1, -1, -1):
        if w < 0:
            break
        board[r][w]
        w -= 1
    w = col + 1
    for r in range(row - 1, -1, -1):
        if w >= len(board):
            break
        board[r][w] = "x"
        w += 1
    w = col - 1
    for r in range(row + 1, len(board)):
        if w < 0:
            break
        board[r][w] = "x"
        w -= 1


def recursive_solve(board, row, queens, solutions):
    '''method: recursive_solve
    recursively solve an N-queens puzzle.
    args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    '''
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for w in range(len(board)):
        if board[row][w] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][w] = "Q"
            xout(tmp_board, row, w)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
