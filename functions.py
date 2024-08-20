# def hello_world():
#     print("Hello world")

# def sums (num1, num2 = 3):
#     if (type(num1) is not int or type(num2) is not int):
#         return
#     return num1 + num2

# total = sums(2)
# print (total)

import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3



def rps():
    game_count = 0
    player_win = 0
    computer_win = 0

    def play_rps():
        nonlocal game_count
        
        player_choice = int(input('''\n Welcome to Rock Paper Scissor Game \n 
        Enter Your choice...
            1 for Rock
            2 for Paper
            3 for Scissor\n'''))

        if player_choice not in [1, 2, 3]:
            print("you must enter 1, 2 or 3")
            return play_rps()

        computer_choice = int(random.choice("123"))

        print(f"You chose {str(RPS(player_choice)).replace("RPS.", "")}")
        print(f"Computer chose {str(RPS(computer_choice)).replace("RPS.", "")}")

        def game_play(player_choice, computer_choice):
            nonlocal player_win
            nonlocal computer_win
            
            if player_choice == 1 and computer_choice == 3:
                player_win += 1
                print("\n🤩You win🎉🏅")
            
            elif player_choice == 2 and computer_choice == 1:
                player_win += 1
                print("\n🤩You win🎉🏅")
            
            elif player_choice == 3 and computer_choice == 2:
                player_win += 1
                print("\n🤩You win🎉🏅")
            
            elif player_choice == computer_choice:
                print("\nGame Draw😐")
            
            else:
                computer_win += 1
                print("\n🤖Computer Wins😒")

        game_result = game_play(player_choice, computer_choice)
        print(game_result)

        game_count += 1

        print(f"\nGame count: {str(game_count)}")
        print(f"\nPlayer win count: {str(player_win)}")
        print(f"\nComputer win count: {str(computer_win)}")

        print("\nDo you want to play again? ")

        while True:
            play_again = input("\n\n Press Y to continue \n Press Q to Quit \n\n")
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_rps()
        else:
            print("T\n🫰Thanks for playing🎉")
            sys.exit("\nBye Bye Bye👋")

    return play_rps
play = rps()

if(__name__) == "__main__":
    play()