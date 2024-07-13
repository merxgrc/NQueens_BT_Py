import random
import numpy as np
import matplotlib.pyplot as plt

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
        nodes_visited = []

        for i in range(1, count + 1):
            self.x = [0] * (self.n + 1)
            self.num_nodes = 0
            self.solve_n_queens()
            total += self.num_nodes
            nodes_visited.append(self.num_nodes)
            print(f"Test: {i}.) nodes visited: {self.num_nodes}")

        avg_nodes_visited = total / count
        print(f"Average nodes visited: {avg_nodes_visited}")

        # Plot histogram of nodes visited
        plt.hist(nodes_visited, bins=20, alpha=0.75)
        plt.xlabel('Nodes Visited')
        plt.ylabel('Frequency')
        plt.title('Distribution of Nodes Visited')
        plt.grid(True)
        plt.show()

        return nodes_visited

    def visualize_board(self):
        board = np.zeros((self.n, self.n))
        for i in range(1, self.n + 1):
            if self.x[i] != 0:
                board[i - 1][self.x[i] - 1] = 1

        fig, ax = plt.subplots()
        ax.matshow(board, cmap=plt.cm.Blues)

        for i in range(self.n):
            for j in range(self.n):
                c = board[j, i]
                if c == 1:
                    ax.text(i, j, 'Q', va='center', ha='center')

        plt.show()

if __name__ == "__main__":
    n = 12
    count = 100
    solver = NQueensMonteCarlo(n)
    nodes_visited = solver.monte_carlo(count)
    solver.visualize_board()

