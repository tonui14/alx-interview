#!/usr/bin/python3
"""
N-Queens problem solver
"""
import sys


def print_solutions(solutions):
    """
    Prints the list of solutions in the required format.

    Args:
        solutions (list): List of solutions, where each solution is a list of
                          [row, column] pairs.
    """
    for solution in solutions:
        print(solution)


def is_safe(board, row, col, n):
    """
    Checks if a queen can be placed at board[row][col].

    Args:
        board (list): Current board state.
        row (int): Row index.
        col (int): Column index.
        n (int): Size of the board.

    Returns:
        bool: True if safe, False otherwise.
    """
    # Check the column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(n, row, board, solutions):
    """
    Solves the N-Queens problem using backtracking.

    Args:
        n (int): Size of the board.
        row (int): Current row.
        board (list): Current board state.
        solutions (list): List to store all valid solutions.
    """
    if row == n:
        # Found a valid solution
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            # Backtrack
            board[row] = -1


def main():
    """
    Entry point of the program. Handles input validation and solution output.
    """
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

    # Initialize board and solutions list
    board = [-1] * n
    solutions = []

    # Solve the N-Queens problem
    solve_nqueens(n, 0, board, solutions)

    # Print all solutions
    print_solutions(solutions)


if __name__ == "__main__":
    main()
