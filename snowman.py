import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


# Snowman ASCII Art stages
STAGES = [
    """
     ___
    /___\\
    (o o)
    ( : )
    ( : )
    """,
    """
     ___
    /___\\
    (o o)
    ( : )
    """,
    """
     ___
    /___\\
    (o o)
    """,
    """
     ___
    /___\\
    """
]


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
    print()


def get_random_word():
    """Select a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """Start the Snowman Meltdown game."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    display_game_state(mistakes, secret_word, guessed_letters)

    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)

    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()