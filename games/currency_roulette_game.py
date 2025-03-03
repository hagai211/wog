import random

from currency_converter import CurrencyConverter


def get_money_interval(num):
    c = CurrencyConverter()
    return int(c.convert(num, 'USD', 'ILS'))


def get_guess_from_user(num):
    while True:
        user_guess = input(f"The generated number is {num}$ \n"
                           "Take a guess what is the converted rate in ILS? ")
        try:
            return int(user_guess)
        except ValueError:
            print("Invalid input, only integers")


def compare_results(guess, answer, allowed_range):
    if guess - allowed_range <= answer <= guess + allowed_range:
        return True
    else:
        return False


def play(difficulty):
    print("generating number...")
    random_number = random.randint(1, 50)
    guess = get_guess_from_user(random_number)
    answer = get_money_interval(random_number)
    allowed_range = 10 - difficulty
    if compare_results(guess, answer, allowed_range):
        print(f"You Win, the answer is {answer} \nacceptable range is {allowed_range}")
        return True
    else:
        print(f"You lose, the answer is {answer} \nacceptable range is {allowed_range}")
        return False
