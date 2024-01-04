#!/usr/bin/python3


""" Backtracking class for nqueens """


class Backtrack:
    """ Backtracking class for nqueens """

    def __init__(self, n):
        """ intialize """
        self.n = n
        self.solutions = []
        self.solve()

    def solve(self):
        """ solve method"""
        self.place_queen(0, [-1] * self.n)

    def place_queen(self, row, state):
        """ place_queen method """
        if row == self.n:
            self.solutions.append(state.copy())
        else:
            for col in range(self.n):
                if self.is_safe(row, col, state):
                    state[row] = [row, col]
                    self.place_queen(row + 1, state)

    def is_safe(self, row, col, state):
        """ checks if a queen can be placed in a row, col """
        for r in range(row):
            if state[r][1] == col or abs(state[r][1] - col) == row - r:
                return False
        return True


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        b = Backtrack(n)
        for state in b.solutions:
            print(state)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
