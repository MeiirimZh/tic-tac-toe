import keyboard
import os

from scripts.utils import check_grid, print_grid


class TwoPlayers:
    def __init__(self, game_state_manager):
        self.game_state_manager = game_state_manager

        self.grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        self.display_grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        self.x = 0
        self.y = 0

        self.turn = "x"
        self.win = "None"
        self.win_text = {"x": "Player 1 wins!\n", "o": "Player 2 wins!\n"}

    def run(self):
        self.display_grid = [row[:] for row in self.grid]

        self.display_grid[self.y][self.x] = "v"

        if self.win == "None":
            if self.turn == "x":
                print("Player 1's (X) turn\n")
            else:
                print("Player 2's (O) turn\n")

            print_grid(self.display_grid)

            key = keyboard.read_key()

            if key == "up":
                self.y = max(0, self.y - 1)
            if key == "down":
                self.y = min(2, self.y + 1)
            if key == "right":
                self.x = min(2, self.x + 1)
            if key == "left":
                self.x = max(0, self.x - 1)
            if key == "enter":
                self.grid[self.y][self.x] = self.turn
                if self.turn == "x":
                    self.turn = "o"
                else:
                    self.turn = "x"

                self.win = check_grid(self.x, self.y, self.grid)
        else:
            print(self.win_text[self.win])

            print_grid(self.grid)

            key = keyboard.read_key()
        
        os.system("cls")
