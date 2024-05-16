#!/usr/bin/env python3
import sys

def print_solution(queens):
    """Format and print the list of queens' positions for a solution."""
    solution = []
    for i in range(len(queens)):
        solution.append([i, queens[i]])
    print(solution)

def is_safe(queens, row, col):
    """Check if it's safe to place a queen at row, col."""
    for i in range(row):
        if queens[i] == col or \
           queens[i] - i == col - row or \
           queens[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, row, queens):
    """Use backtracking to find all solutions for the n-queens problem."""
    if row == n:
        print_solution(queens)
    else:
        for col in range(n):
            if is_safe(queens, row, col):
                queens[row] = col
                solve_nqueens(n, row + 1, queens)
                queens[row] = -1

def nqueens(n):
    """Initialize and start the N Queens problem solution."""
    queens = [-1] * n
    solve_nqueens(n, 0, queens)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(n)
