import time
import keyboard
import random
import os

from scripts.utils import print_grid, find_pair, check_grid


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

        self.choose_char()

        self.turn = random.choice(["x", "o"])

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
                # Player's turn
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

                    self.turns += 1

                    self.win = check_grid(self.y, self.x, self.grid)

                    if self.win == self.player:
                        self.win = self.player
                        self.player_wins += 1

                    if self.win == "none" and self.turns == 9:
                        self.win = "draw"

                    self.turn = self.ai
            else:
                # AI's turn
                print_grid(self.grid)

                move = find_pair(self.grid)
                ai_x = 0
                ai_y = 0

                if move:
                    # Tactic: blocking
                    self.grid[move[0]][move[1]] = self.ai
                    ai_x = move[1]
                    ai_y = move[0]
                else:
                    # Tactic: advance
                    moved = False
                    while not moved:
                        x = random.randint(0, 2)
                        y = random.randint(0, 2)
                        if self.grid[y][x] == " ":
                            self.grid[y][x] = self.ai

                            ai_x = x
                            ai_y = y

                            moved = True

                self.turns += 1

                self.win = check_grid(ai_y, ai_x, self.grid)
                
                if self.win == self.ai:
                    self.win = self.ai
                    self.ai_wins += 1

                if self.win == "none" and self.turns == 9:
                    self.win = "draw"

                time.sleep(.85)

                self.turn = self.player
        else:
            if self.win == self.player:
                print("Player wins!\n")
            elif self.win == self.ai:
                print("Computer wins!\n")
            else:
                print("Draw!\n")

            print_grid(self.grid)

            print("\nPress [Enter] to restart the game")

            key = keyboard.read_key()

            if key == "enter":
                self.restart_game()

        os.system("cls")
