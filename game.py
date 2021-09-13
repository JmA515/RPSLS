from human import Human
from ai import Artificial

class Game:
    def __init__(self):
        pass

    def welcome_rules(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock (RPSLS)!\n"
        "\n"
        "The rules of RPSLS is:\n"
        "\n"
        "Rock crushes Scissors\n"
        "Scissors cuts Paper\n"
        "Paper covers Rock\n"
        "Rock crushes Lizard\n"
        "Lizard poisons Spock\n"
        "Spock smashes Scissors\n"
        "Scissors decapitates Lizard\n"
        "Lizard eats Paper\n"
        "Paper disproves Spock\n"
        "Spock vaporizes Rock\n"
        "\n"
        "Let's play!")
    
    def game_mode(self):
        game_choice = int(input("How will you be playing?\n"
        "(Press 1) for single player\n"
        "(Press 2) for multiplayer  "))
        if game_choice == 1:
            self.ai_game()
        elif game_choice == 2:
            self.human_game()
        else:
            self.game_mode()
        pass

    def ai_game(self):
        self.human1_turn()
        self.ai_turn()


        self.human1_turn()
        self.ai_turn()
      

        #if 1 player has 2 round wins, game over 
        #else
            # self.human1_turn()
            # self.ai_turn()

    def ai_turn(self):
        ai_player = Artificial()
        ai_player_choice = ai_player.choose_gesture()
        print(ai_player_choice)
        pass

    def human1_turn(self):
        human_player1 = Human()
        human_player1.choose_gesture()
        human1_choice = self.valid_answer()
        print(human1_choice)

    def human_game(self):
        pass        

    def run_game(self):
        pass

    def valid_answer(self):
        while True:
            choice = input("Please type your RPSLS gesture choice here: ").casefold()
            if choice.lower() not in ("rock", "paper", "scissors", "lizard", "spock"):
                print("Please retype your gesture choice.")
            else:
                break
        return choice
