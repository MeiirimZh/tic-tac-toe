import keyboard
import os


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

    def run(self):
        self.display_grid = [row[:] for row in self.grid]

        self.display_grid[self.y][self.x] = "v"

        for row in self.display_grid:
            for column in row:
                print(f'[{column}]', end="")
            print()
        
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
        
        os.system("cls")
