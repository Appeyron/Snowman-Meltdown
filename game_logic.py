import random

from ascii_art import STAGES


WORDS = [
    "python",
    "git",
    "github",
    "snowman",
    "meltdown",
]


def get_random_word():
    """Select a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current snowman stage and hidden word."""
    print("\n" + "=" * 30)
    print("Snowman Meltdown")
    print("=" * 30)
    print(STAGES[mistakes])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(f"Word:            {display_word}")
    print(f"Mistakes:        {mistakes}/{len(STAGES) - 1}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print("=" * 30)


def is_word_guessed(secret_word, guessed_letters):
    """Check whether all letters of the secret word were guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False

    return True


def get_valid_guess(guessed_letters):
    """Ask the user for a valid single alphabetical character."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue

        if not guess.isalpha():
            print("Please enter only alphabetical characters.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        return guess


def play_game():
    """Start one round of Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while (
        mistakes < max_mistakes
        and not is_word_guessed(secret_word, guessed_letters)
    ):
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_guess(guessed_letters)
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
        print(f"The secret word was: {secret_word}")


def ask_for_replay():
    """Ask the user whether they want to play again."""
    while True:
        answer = input("Do you want to play again? (y/n): ").lower().strip()

        if answer == "y":
            return True

        if answer == "n":
            return False

        print("Please enter y or n.")


def main():
    """Run the game and handle replay."""
    while True:
        play_game()

        if not ask_for_replay():
            print("Thanks for playing!")
            break