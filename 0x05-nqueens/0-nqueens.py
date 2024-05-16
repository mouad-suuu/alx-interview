#!/usr/bin/python3
"""
Usage:
    ./0-nqueens.py N
where N is the number of queens and the size of the chessboard.
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at (row, col).
    Parameters:
        board (list): Current state of the board (columns with queens placed).
        row (int): Target row for placing the queen.
        col (int): Target column for placing the queen.
    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens_util(board, row, n):
    """
    Recursive utility function to solve the
    N Queens problem using backtracking.
    Parameters:
        board (list): Current partial configuration of the board.
        row (int): Current row to try to place a queen.
        n (int): Total number of queens and size of the board.
    """
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_util(board, row + 1, n)
            board[row] = -1


def solve_nqueens(n):
    """
    Set up the board and start the backtracking algorithm.
    Parameters:
        n (int): Number of queens and the size of the chessboard.
    """
    board = [-1] * n
    solve_nqueens_util(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(N)
