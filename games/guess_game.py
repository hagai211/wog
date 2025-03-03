import random


def generate_number(difficulty):
    secret_number = random.randint(0, difficulty)
    print("Secret number has been saved")
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"please enter a number between 0 to {difficulty}: "))
            if 0 <= guess <= difficulty:
                return guess
            else:
                print("Please enter a valid number")
        except ValueError:
            print("Invalid input, please a enter a valid number")


def compare_results(secret_number, guess):
    return secret_number == guess


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    if compare_results(secret_number, guess):
        print("You win!")
        return True
    else:
        print(f"you lose! the correct number is {secret_number}")
        return False
