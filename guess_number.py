import sys
import random

def guess(name='Player'):
    game_count = 0
    player_wins = 0
    def play_guess():
        nonlocal player_wins

        print("")
        playerchoice = input(f"\n{name}, guess which number I'm thinking of....1, 2, or 3.\n\n")

        if playerchoice not in ['1','2','3']:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess()
        choice = int(playerchoice)
        print("")

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print(f"\n{name}, you chose {playerchoice}")
        print(f"I was thinking about the number {computer_choice}")
        print("")

        def decide_winner(choice,computer):
            nonlocal name
            nonlocal player_wins
            
            if choice == computer:
                player_wins += 1
                print(f"🎉{name}, you win!")
            else:
                print(f"Sorry, {name}. Better luck next time.")
            
        decide_winner(choice,computer)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {(player_wins/game_count)*100}")
        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or\nQ to Quit ")
            if playagain.lower() not in ['y','q']:
                continue
            else:
                break      

        if playagain.lower() == 'y':
                return play_guess()
        else:
            print("\nThank you for playing!")
            sys.exit(f"Bye {name}! 👋🏻")

    return play_guess


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guess_number = guess(args.name)
    guess_number()
