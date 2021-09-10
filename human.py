from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        print("Here are your choices.")
        index = 0
        for gesture in self.gesture:
            print(f"Press {index} for {gesture}")
            index += 1