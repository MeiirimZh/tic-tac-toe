import keyboard
import random
import os

from scripts.utils import print_grid, find_pair


class VersusAI:
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

        self.player = ""
        self.ai = ""

        self.turn = random.choice(["x", "o"])

        self.turns = 0

        self.win = "none"
        self.win_text = {"x": "Player 1 wins!\n", "o": "Player 2 wins!\n", "draw": "Draw!\n"}
        self.player_wins = 0
        self.ai_wins = 0

        self.choose_char()

    def choose_char(self):
        chars = ["x", "o"]
        random.shuffle(chars)
        self.player, self.ai = chars

    def restart_game(self):
        self.grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        self.x = 0
        self.y = 0

        self.player = "x" if self.player == "o" else "o"

        self.win = "none"

        self.turns = 0

    def run(self):
        self.display_grid = [row[:] for row in self.grid]

        self.display_grid[self.y][self.x] = "v"

        if self.win == "none":
            print(f'Player wins: {self.player_wins}\tComputer wins: {self.ai_wins}')

            if self.player == self.turn:
                print(f"Player's ({self.player}) turn\n")
            else:
                print(f"Computer's ({self.ai}) turn. Computer is thinking...\n")

            if self.player == self.turn:
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
                    if self.grid[self.y][self.x] != "x" and self.grid[self.y][self.x] != "o":
                        self.grid[self.y][self.x] = self.player

                    self.turn = self.ai
            else:
                print_grid(self.grid)

                find_pair(self.grid)

                key = keyboard.read_key()

        os.system("cls")
