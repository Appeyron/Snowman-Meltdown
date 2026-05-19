import random

from ascii_art import STAGES


WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Select a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current snowman stage and hidden word."""
    print(STAGES[mistakes])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Mistakes:", mistakes)
    print()


def is_word_guessed(secret_word, guessed_letters):
    """Check whether all letters of the secret word were guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False

    return True


def play_game():
    """Start the Snowman Meltdown game."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes and not is_word_guessed(
        secret_word,
        guessed_letters
    ):
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            mistakes += 1

    display_game_state(mistakes, secret_word, guessed_letters)

    if is_word_guessed(secret_word, guessed_letters):
        print("You saved the snowman!")
    else:
        print("The snowman melted!")
        print("The secret word was:", secret_word)


if __name__ == "__main__":
    play_game()