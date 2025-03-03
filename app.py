from games import guess_game, currency_roulette_game, memory_game

from score import add_score


def welcome():
    username = input("Hello!\nwhat is your name?\n")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def start_play():
    while True:
        try:
            selection = int(
                input("Please choose a game to play:\n1.Memory Game - a sequence of numbers will appear for 1 second "
                      "and you have to guess it back.\n2.Guess Game - guess a number and see if you chose like the "
                      "computer.\n3.Currency Roulette - try and guess the value of a random amount of USD in "
                      "ILS\nYour pick: "))
            if selection not in [1, 2, 3]:
                print("Not Valid, choose again")
                continue
            print(f"you chose option {selection}")
            difficulty_level = int(input("Select a difficulty level 1 to 5: "))
            if difficulty_level not in [1, 2, 3, 4, 5]:
                print("Please select a difficulty level between 1 to 5 as requested")
                continue
            # Map selection numbers to game functions
            games = {
                1: memory_game.play,
                2: guess_game.play,
                3: currency_roulette_game.play
            }
            # Execute the selected game
            if selection in games:
                user_won = games[selection](difficulty_level)
                if user_won:
                    print('Updating score...')
                    add_score(difficulty_level)
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid input, choose again...")
            continue
        play_again = input("Do you want to play again? y/n ")
        while play_again != 'y' and play_again != 'n':
            play_again = input("Do you want to play again? y/n ")
        if play_again == 'n':
            print('Goodbye, have a nice day')
            break

