#!/usr/bin/python3
""" nqueens problem solution module"""
import sys


def backtrack(r, n, cols, pos_diag, neg_diag, board):
    """ backtrack function """
    if r == n:
        res = []
        for i in range(len(board)):
            for k in range(len(board[i])):
                if board[i][k] == 1:
                    res.append([i, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
            continue

        cols.add(c)
        pos_diag.add(r + c)
        neg_diag.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, pos_diag, neg_diag, board)

        cols.remove(c)
        pos_diag.remove(r + c)
        neg_diag.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """ Solution to nqueens problem """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(n[1])
        if size < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(size)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
