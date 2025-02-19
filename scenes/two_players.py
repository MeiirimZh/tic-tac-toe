import keyboard
import os
import sys

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
        self.player_1_wins = 0
        self.player_2_wins = 0

        self.options = ["Restart", "Return to menu", "Quit"]
        self.current_option = 0

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

        self.turns = 0

    def run(self):
        self.display_grid = [row[:] for row in self.grid]

        self.display_grid[self.y][self.x] = "v"

        if self.win == "none":
            print(f'Player 1 wins: {self.player_1_wins}\tPlayer 2 wins: {self.player_2_wins}')

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
            if key == "esc":
                self.game_state_manager.set_state("Menu")
            if key == "enter":
                if self.grid[self.y][self.x] != "x" and self.grid[self.y][self.x] != "o":
                    self.grid[self.y][self.x] = self.player_turn
                    if self.player_turn == "x":
                        self.player_turn = "o"
                    else:
                        self.player_turn = "x"

                self.turns += 1

                self.win = check_grid(self.y, self.x, self.grid)

                if self.win == "x":
                    self.player_1_wins += 1
                elif self.win == "o":
                    self.player_2_wins += 1
                else:
                    if self.turns == 9:
                        self.win = "draw"
                
        else:
            print(self.win_text[self.win])

            print_grid(self.grid)
            print("\n")

            for option in self.options:
                if self.options.index(option) == self.current_option:
                    print(f'> {option}')
                else:
                    print(option)

            key = keyboard.read_key()

            if key == "up":
                self.current_option = max(0, self.current_option - 1)
            if key == "down":
                self.current_option = min(2, self.current_option + 1)
            if key == "enter":
                if self.current_option == 0:
                    self.restart_game()
                elif self.current_option == 1:
                    self.game_state_manager.set_state("Menu")
                else:
                    sys.exit()
        
        os.system("cls")
