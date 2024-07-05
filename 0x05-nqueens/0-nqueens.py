#!/usr/bin/python3
""" N queens """
import sys

# Ensure correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# Ensure the argument is a digit
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

n = int(sys.argv[1])

# Ensure N is at least 4
if n < 4:
    print("N must be at least 4")
    exit(1)

def queens(n, row=0, columns=[], diagonals1=[], diagonals2=[]):
    """ Generate all valid solutions for the n-queens problem """
    if row == n:
        yield columns
    else:
        for col in range(n):
            if col not in columns and row + col not in diagonals1 and row - col not in diagonals2:
                yield from queens(n, row + 1, columns + [col], diagonals1 + [row + col], diagonals2 + [row - col])

def solve(n):
    """ Solve the n-queens problem and print each solution """
    for solution in queens(n):
        print([[i, solution[i]] for i in range(n)])

solve(n)

