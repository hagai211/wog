from utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def add_score(difficulty):
    POINTS_OF_WINNING = difficulty * 3 + 5
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read()) + POINTS_OF_WINNING
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(current_score))
    except FileNotFoundError:
        return BAD_RETURN_CODE
