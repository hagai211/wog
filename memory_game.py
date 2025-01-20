import random
import time
from utils import screen_cleaner


def generate_sequence(difficulty):
    lst = []
    for i in range(difficulty):
        j = random.randint(1, 101)
        lst.append(j)
    return lst


def get_list_from_user():
    while True:
        try:
            user_input = input("What are the Numbers? \nEnter numbers separated by spaces: ")  # Example: "34 72 49"
            user_answer = list(map(int, user_input.split()))
            is_max_under_101 = True
            for i in user_answer:
                if i > 100:
                    is_max_under_101 = False
                    print("The highest possible value is 100, try again")
            if is_max_under_101:
                return user_answer
        except ValueError:
            print("Please enter valid numbers separated by spaces.")


def is_list_equal(generated_sequence, user_list):
    return generated_sequence == user_list


def play(difficulty):
    sequence = generate_sequence(difficulty)
    print(sequence)
    time.sleep(0.7)
    screen_cleaner()
    user_answer = get_list_from_user()
    if is_list_equal(sequence, user_answer):
        print("You Win")
        return True
    else:
        print(f"You Lose, the numbers were {sequence}")
        return False
