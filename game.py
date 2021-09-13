from human import Human
from ai import Artificial

class Game:
    def __init__(self):
        self.contestants = []
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
        "Type (1) for single player\n"
        "Type (2) for multiplayer  "))
        if game_choice == 1:
            ai_player = Artificial()
            self.contestants.append(ai_player)
            human_player1 = Human()
            self.contestants.append(human_player1)
            self.ai_game()
        elif game_choice == 2:
            human_player1 = Human()
            self.contestants.append(human_player1)
            human_player2 = Human()
            self.contestants.append(human_player2)
            self.human_game()
        else:
            self.game_mode()
        pass

    def ai_game(self):
        human_winner_counter = 0
        ai_winner_counter = 0

        human_round1 = self.human1_turn()
        ai_round1 = self.ai_turn()
        round_one_winner = self.find_round_winner(human_round1, ai_round1)
        print(round_one_winner)
        if round_one_winner == f'{self.contestants[1].name} wins!':
            human_winner_counter += 1
        elif round_one_winner == f'{self.contestants[0].name} wins!':
            ai_winner_counter += 1
        
        human_round2 = self.human1_turn()
        ai_round2 = self.ai_turn()
        round_two_winner = self.find_round_winner(human_round2, ai_round2)
        print(round_two_winner)
        if round_two_winner == f'{self.contestants[1].name} wins!':
            human_winner_counter += 1
        elif round_two_winner == f'{self.contestants[0].name} wins!':
            ai_winner_counter += 1
        if human_winner_counter == 2:
            print(f'{self.contestants[1].name} wins!!!')
        elif ai_winner_counter == 2:
            print(f'{self.contestants[0].name} wins!!!\n''Better luck next time! ¯\_(ツ)_/¯')
        elif human_winner_counter < 2 and ai_winner_counter < 2:
            human_round3 = self.human1_turn()
            ai_round3 = self.ai_turn()
            round_three_winner = self.find_round_winner(human_round3, ai_round3)
            print(round_three_winner)
            if round_three_winner == f'{self.contestants[1].name} wins!':
                human_winner_counter += 1
            elif round_three_winner == f'{self.contestants[0].name} wins!':
                ai_winner_counter += 1
            
            if human_winner_counter >= 2:
                print(f'{self.contestants[1].name} wins!!!')
            elif ai_winner_counter >= 2:
                print(f'{self.contestants[0].name} wins!!!\n''Better luck next time! ¯\_(ツ)_/¯')
            elif human_winner_counter == 1 and ai_winner_counter == 0:
                print(f'{self.contestants[1].name} wins!!!') 
            elif ai_winner_counter == 1 and human_winner_counter == 0:
                print(f'{self.contestants[0].name} wins!!!\n''Better luck next time! ¯\_(ツ)_/¯')
            elif human_winner_counter == ai_winner_counter:
                print("How does it feel to tie and win nothing?! Sucks right?\n""Play again because if you ain't first, you're last!")

    def ai_turn(self):
        ai_player_choice = self.contestants[0].choose_gesture()
        print(ai_player_choice)
        return ai_player_choice

    def human1_turn(self):
        self.contestants[1].choose_gesture()
        human1_choice = self.valid_answer()
        print(human1_choice)
        return human1_choice

    def human_game(self):
        pass        

    def run_game(self):
        pass

    def valid_answer(self):
        while True:
            choice = input("Please type your RPSLS gesture choice here: ").casefold()
            if choice.lower() not in ("rock", "paper", "scissors", "lizard", "spock"):
                print("Please re-type your gesture choice.")
            else:
                break
        return choice

    def find_round_winner(self, human1_choice, ai_player_choice):
        if human1_choice == ai_player_choice:
            return"It's a tie."

        elif human1_choice == "rock":   
            if ai_player_choice == "scissors" or ai_player_choice ==  "lizard":
                return f'{self.contestants[1].name} wins!'
            elif ai_player_choice == "spock" or ai_player_choice == "paper":
                return f'{self.contestants[0].name} wins!'

        elif human1_choice == "paper":
            if ai_player_choice == "spock" or ai_player_choice == "rock":   
                return f'{self.contestants[1].name} wins!'
            elif ai_player_choice == "lizard" or ai_player_choice == "scissors":
                return f'{self.contestants[0].name} wins!'

        elif human1_choice == "scissors":
            if ai_player_choice == "paper" or ai_player_choice == "lizard":
                return f'{self.contestants[1].name} wins!'
            elif ai_player_choice == "rock" or ai_player_choice == "spock":
                return f'{self.contestants[0].name} wins!'

        elif human1_choice == "lizard":
            if ai_player_choice == "spock" or ai_player_choice == "paper":
                return f'{self.contestants[1].name} wins!'
            elif ai_player_choice == "rock" or ai_player_choice == "scissors":
                return f'{self.contestants[0].name} wins!'

        elif human1_choice == "spock":
            if ai_player_choice == "rock" or ai_player_choice == "scissors":
                return f'{self.contestants[1].name} wins!'
            elif ai_player_choice == "paper" or ai_player_choice == "lizard":
                return f'{self.contestants[0].name} wins!'
