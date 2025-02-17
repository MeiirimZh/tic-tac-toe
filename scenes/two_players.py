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

        self.player_turn = "x"
        self.turns = 0

        self.win = "none"
        self.win_text = {"x": "Player 1 wins!\n", "o": "Player 2 wins!\n", "draw": "Draw!\n"}

    def restart_game(self):
        self.grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        self.x = 0
        self.y = 0

        self.player_turn = "x"
        self.win = "none"

    def run(self):
        self.display_grid = [row[:] for row in self.grid]

        self.display_grid[self.y][self.x] = "v"

        if self.win == "none":
            if self.player_turn == "x":
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
                if self.grid[self.y][self.x] != "x" and self.grid[self.y][self.x] != "o":
                    self.grid[self.y][self.x] = self.player_turn
                    if self.player_turn == "x":
                        self.player_turn = "o"
                    else:
                        self.player_turn = "x"

                self.turns += 1

                self.win = check_grid(self.y, self.x, self.grid)

                if self.turns == 9 and self.win == "none":
                    self.win = "draw"
                
        else:
            print(self.win_text[self.win])

            print_grid(self.grid)

            print("\nPress [Enter] to restart the game")

            key = keyboard.read_key()

            if key == "enter":
                self.restart_game()
        
        os.system("cls")
