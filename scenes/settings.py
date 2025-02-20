import keyboard
import os


class Settings:
    def __init__(self, game_state_manager, data):
        self.game_state_manager = game_state_manager
        self.data = data

        self.tabs = ["Main", "Cursor", "Random AI behavior"]
        self.current_tab = 0

        self.options = ["Cursor", "Random AI behavior", "Exit"]
        self.current_option = 0

        self.cursor_options = ["v", "*", ":", "#", "$", "@"]
        self.current_cursor_option = 0

        self.random_ai_options = ["On", "Off"]
        self.current_random_ai_option = 0

        self.commands = {"Cursor": lambda: self.change_tab(1), "Random AI behavior": lambda: self.change_tab(2), "Exit": lambda: self.game_state_manager.set_state("Menu")}

    def change_tab(self, tab):
        self.current_tab = tab 

    def run(self):
        if self.current_tab == 0:
            print("Settings\n")

            for option in self.options:
                if option == self.options[self.current_option]:
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
        elif self.current_tab == 1:
            print("Cursor\n")

            print(f'< {self.cursor_options[self.current_cursor_option]} >')

            print("\nPress [Escape] to return to settings")

            key = keyboard.read_key()

            if key == "left":
                self.current_cursor_option = max(0, self.current_cursor_option - 1)
            if key == "right":
                self.current_cursor_option = min(len(self.cursor_options)-1, self.current_cursor_option + 1)
            if key == "enter":
                self.data.cursor = self.cursor_options[self.current_cursor_option]
            if key == "esc":
                self.current_tab = 0
        else:
            print("Random AI behavior\n")

            for option in self.random_ai_options:
                if option == self.random_ai_options[self.current_random_ai_option]:
                    print(f'> {option}')
                else:
                    print(option)

            print("\nPress [Escape] to return to settings")

            key = keyboard.read_key()

            if key == "up":
                self.current_random_ai_option = max(0, self.current_random_ai_option - 1)
            if key == "down":
                self.current_random_ai_option = min(len(self.random_ai_options)-1, self.current_random_ai_option + 1)
            if key == "enter":
                if self.current_random_ai_option == 0:
                    self.data.random_ai_behavior = True
                else:
                    self.data.random_ai_behavior = False
            if key == "esc":
                self.current_tab = 0

        os.system("cls")
