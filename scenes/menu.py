import keyboard
import os
import sys


class Menu:
    def __init__(self, game_state_manager):
        self.game_state_manager = game_state_manager

        self.options = ["Player vs Computer", "Player vs Player", "Settings", "Quit"]
        self.current_option = 0

    def run(self):
        print("Tic Tac Toe\n")

        for option in self.options:
            if option == self.options[self.current_option]:
                print(f'> {option}')
            else:
                print(option)

        print("\nMade by Zhanzhumanov Meiirim 2025")

        key = keyboard.read_key()

        if key == "up":
            self.current_option = max(0, self.current_option - 1)
        if key == "down":
            self.current_option = min(len(self.options)-1, self.current_option + 1)
        if key == "enter":
            # Player vs Computer
            if self.current_option == 0:
                self.game_state_manager.set_state("Versus AI")
            # Player vs Player
            elif self.current_option == 1:
                self.game_state_manager.set_state("Two Players")
            # Settings
            elif self.current_option == 2:
                self.game_state_manager.set_state("Settings")
            # Quit
            else:
                sys.exit()

        os.system("cls")
