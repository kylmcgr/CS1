import random

def make_random_code():
    """make_random_code creates a random code for Mastermind game. It
    takes no input and returns a 4 letter string of 'R', 'G', 'B', 'Y',
    'O', or 'W'"""
    code = ""
    for i in range(4):
        code += random.choice(['R', 'G', 'B', 'Y', 'O', 'W'])
    return code

def count_exact_matches(code, guess):
    """count_exact_matches checks to see how many of the colors guessed
    are exact matches for the code. Takes 2 strings of length 4 as
    inputs and returns the number of exact matches"""
    right = 0
    for i in range(4):
        if guess[i] == code[i]:
            right += 1
    return right

def count_letter_matches(code, guess):
    """count_letter_matches checks to see how many of the colors guessed
    are matches for the code. Takes 2 strings of length 4 as inputs and
    returns the number of matches"""
    right = 0
    code = list(code)
    for i in range(4):
        if guess[i] in code:
            right += 1
            code.remove(guess[i])
    return right

def compare_codes(code, guess):
    """compare_codes checks the exact matches and letter matches of
    the guess and the code. Takes 2 strings of length 4 as inputs and
    returns a 4 legnth string representing the about of exact and letter
    matches."""
    right = ""
    b = count_exact_matches(code, guess)
    w = count_letter_matches(code, guess) - b
    rest = 4 - b - w
    right += "b" * b
    right += "w" * w
    right += "-" * rest
    return right

def run_game():
    print("New game.")
    result = "----"
    code = make_random_code()
    n = 0
    while result != "bbbb":
        guess = input("Enter your guess: ")
        n += 1
        result = compare_codes(code, guess)
        print("Result: {}".format(result))
    print("Congratulations! You cracked the code in {} moves!".format(n))
