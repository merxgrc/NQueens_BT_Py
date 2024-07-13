import random
import numpy as np

class NQueensMonteCarlo:
    def __init__(self, n):
        self.n = n
        self.x = [0] * (n + 1)
        self.num_nodes = 0

    def solve_n_queens(self):
        m = 1
        mprod = 1
        i = 1

        while m != 0 and i <= self.n:
            mprod *= m
            self.num_nodes += mprod * self.n
            prom_children = []
            m = 0
            for j in range(1, self.n + 1):
                if self.is_promising(i, j):
                    m += 1
                    prom_children.append(j)
            if prom_children:
                random.shuffle(prom_children)
                self.x[i] = prom_children[0]
            i += 1

    def is_promising(self, column, row):
        for j in range(1, column):
            if self.x[j] == row or abs(self.x[j] - row) == abs(j - column):
                return False
        return True

    def monte_carlo(self, count):
        total = 0
        for i in range(1, count + 1):
            self.x = [0] * (self.n + 1)
            self.num_nodes = 0
            self.solve_n_queens()
            total += self.num_nodes
            print(f"Test: {i}.) nodes visited: {self.num_nodes}")
        print(f"Average nodes visited: {total / count}")

if __name__ == "__main__":
    n = 12
    count = 20
    solver = NQueensMonteCarlo(n)
    solver.monte_carlo(count)
