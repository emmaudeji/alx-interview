#!/usr/bin/python3
"""Module N-queens"""
import sys


def nqueens(n: int, y: int, board):
    """
    will do the backtracking
    """
    for x in range(n):
        hold = 0
        for q in board:
            if x == q[1]:
                hold = 1
                break
            if y - x == q[0] - q[1]:
                hold = 1
                break
            if x - q[1] == q[0] - y:
                hold = 1
                break
        if hold == 0:
            board.append([y, x])
            if y != n - 1:
                nqueens(n, y + 1, board)
            else:
                print(board)
            del board[-1]


if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(int(sys.argv[1]), 0, [])
