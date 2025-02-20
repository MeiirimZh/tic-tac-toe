import keyboard
import os


class Settings:
    def __init__(self, game_state_manager, data):
        self.game_state_manager = game_state_manager
        self.data = data

        self.options = ["Cursor", "Random AI behavior", "Exit"]
        self.current_option = 0

        self.commands = {"Cursor": "", "Random AI behavior": "", "Exit": lambda: self.game_state_manager.set_state("Menu")}

    def run(self):
        print("Settings\n")

        for option in self.options:
            if option == self.options[self.current_option]:
                if option == "Random AI behavior":
                    pass
                print(f'> {option}')
            else:
                print(option)

        key = keyboard.read_key()

        if key == "up":
            self.current_option = max(0, self.current_option - 1)
        if key == "down":
            self.current_option = min(len(self.options)-1, self.current_option + 1)
        if key == "enter":
            self.commands[self.options[self.current_option]]()

        os.system("cls")
