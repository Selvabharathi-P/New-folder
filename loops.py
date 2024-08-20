import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

play_again = True

while play_again:

    player_choice = int(input('''\n Welcome to Rock Paper Scissor Game \n 
    Enter Your choice...
        1 for Rock
        2 for Paper
        3 for Scissor\n'''))

    if player_choice < 1 or player_choice > 3:
        sys.exit("You must enter 1, 2 or 3")



    computer_choice = int(random.choice("123"))

    print("You chose " + str(RPS(player_choice)).replace("RPS.", ""))
    print("Computer chose " + str(RPS(computer_choice)).replace("RPS.", ""))

    if player_choice == 1 and computer_choice == 3:
        print("\n🤩You win🎉🏅")
    elif player_choice == 2 and computer_choice == 1:
        print("\n🤩You win🎉🏅")
    elif player_choice == 3 and computer_choice == 2:
        print("\n🤩You win🎉🏅")
    elif player_choice == computer_choice:
        print("\nGame Draw😐")
    else:
        print("\n🤖Computer Wins😒")

    play_again = input("\nDo you want to play again? \n\n Press Y to continue \n Press Q to Quit \n\n")
    if play_again.lower() == "y":
        continue
    else:
        print("T\n🫰Thanks for playing🎉")
        play_again = False

sys.exit("\nBye Bye Bye👋")

