"""Wordle game"""

__author__: str = "730826103"


def contains_char(word: str, char: str) -> bool:

    assert len(char) == 1, f"len('{char}') is not 1"

    i: int = 0  # using to interate through word
    while i < len(word):
        if word[i] == char:
            return True  # Found Character
        i += 1
    return False  # Character Not Found


def emojified(guess: str, secret: str) -> str:

    assert len(guess) == len(secret), "Guess and secret word must have the same length."

    result: str = ""  # Initialize empty emoji result string
    i: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while i < len(guess):
        if guess[i] == secret[i]:
            result += GREEN_BOX  # Correct position
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX  # Exists but wrong position
        else:
            result += WHITE_BOX  # Not exist in secret
        i += 1  # incrementing

    return result


def input_guess(expected_length: int) -> str:
    """Ensure the correct length and returns it when it valid"""

    guess: str = input(f"Enter a {expected_length} character word: ")

    while (
        len(guess) != expected_length
    ):  # keey trying until entering a word with correct length
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess  # get a valid input


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    max_turns: int = 6  # Maximum numbers of tries
    turn: int = 1

    while turn <= max_turns:  # player has up to 6 tries
        print(f"=== Turn {turn}/{max_turns} ===")  # turn number

        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))  # show feedback of guess

        if guess == secret:  # check if the guess is correct
            print(f"You won in {turn}/{max_turns} turns!")
            return  # exit
        turn += 1  # go to the next turn
    print("X/6 - Sorry, try again tomorrow!")  # if players run out of turns


if __name__ == "__main__":
    main(secret="codes")
