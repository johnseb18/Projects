"""Making a structured wordle."""


__author__ = "Johnseb18"


def contains_char(p_one: str, i: str) -> bool:
    """Function will return true if single character of second string is at any index, else return False."""
    assert len(i) == 1
    index: int = 0
    while index < len(p_one):
        if p_one[index] == i:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Given a guess and a secret, it will return an emoji according to its correctness."""
    assert len(guess) == len(secret)   # This makes sure the correct length of guess is submitted
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            emoji += YELLOW_BOX
        else: 
            emoji += WHITE_BOX 
        i += 1
    return emoji


def input_guess(length: int) -> str:
    """Given expected length, prompt user for guess until expected length is given."""
    guess = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Function establishes secret, keeps track of turns, and decides if user has won the game
    secret: str = "codes"
    turns: int = 1
    win: bool = False
    while turns < 7 and win is False:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))  # This calls the function input_guess with the length of the secret as the length
        print(emojified(guess, secret))
        turns += 1
        if guess == secret:
            print(f"You won in {turns - 1}/6 turns!")
            win = True
        elif turns > 6: 
            print("X/6 - Sorry, try again tomorrow!")