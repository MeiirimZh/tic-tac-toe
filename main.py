import keyboard
import time

from scenes.two_players import TwoPlayers


class Game:
    def __init__(self):
        self.game_state_manager = GameStateManager("Two Players")
        self.two_players = TwoPlayers(self.game_state_manager)

        self.states = {"Two Players": self.two_players}

    def run(self):
        while True:
            self.states[self.game_state_manager.get_state()].run()

            time.sleep(.2)


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state

    def get_state(self):
        return self.current_state
    
    def set_state(self, state):
        self.current_state = state


if __name__ == "__main__":
    game = Game()
    game.run()
