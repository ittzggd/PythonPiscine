import sys


def count_letters():
    """
    This script counts various types of characters in a given text input.

    Functions:
    - count_letters(): Reads text input from a command-line argument
    or standard input, then counts total characters, upper and
    lower case letters, punctuation marks, spaces, and digits.
    Prints the counts.
    """

    total: int = 0
    lower: int = 0
    upper: int = 0
    punctuation: int = 0
    space: int = 0
    digit: int = 0
    punctuations = r'[!\"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]'

    n = len(sys.argv)

    if n > 2:
        raise AssertionError(": more than one argument is provided")

    if n < 2 or sys.argv[1] is None:
        print("What is the text to count?")
        text = sys.stdin.read()
    else:
        text = sys.argv[1]

    for letter in text:
        if letter.islower():
            lower += 1
        elif letter.isupper():
            upper += 1
        elif letter == ' ' or letter == '\n' or letter == '\r':
            space += 1
        elif letter.isdigit():
            digit += 1
        elif letter in punctuations:
            punctuation += 1
        total += 1

    print(f"The text contains {total} characters")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    '''
    Main function to execute the character counting script.
    '''
    try:
        count_letters()
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
