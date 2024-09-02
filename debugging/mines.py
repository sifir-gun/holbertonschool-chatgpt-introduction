#!/usr/bin/python3
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.marked = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                elif self.marked[y][x]:
                    print('F', end=' ')  # Flag for a mine
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < self.width and 0 <= new_y < self.height:
                    if (new_y * self.width + new_x) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_x, new_y = x + dx, y + dy
                    if (0 <= new_x < self.width and 0 <= new_y < self.height
                            and not self.revealed[new_y][new_x]):
                        self.reveal(new_x, new_y)
        return True

    def mark(self, x, y):
        self.marked[y][x] = not self.marked[y][x]

    def play(self):
        while True:
            self.print_board()
            try:
                action = input(
                    "Enter 'r' to reveal or 'm' to mark, "
                    "followed by coordinates (e.g., 'r 3 4'): "
                ).split()
                if len(action) == 3:
                    cmd, x, y = action[0], int(action[1]), int(action[2])
                    if 0 <= x < self.width and 0 <= y < self.height:
                        if cmd == 'r':
                            if not self.reveal(x, y):
                                self.print_board(reveal=True)
                                print("Game Over! You hit a mine.")
                                break
                        elif cmd == 'm':
                            self.mark(x, y)
                    else:
                        print("Coordinates out of bounds. Try again.")
                else:
                    print("Invalid input. "
                          "Please use the format 'r x y' or 'm x y'.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
