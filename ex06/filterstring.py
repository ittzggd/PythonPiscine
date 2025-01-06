from ft_filter import ft_filter
import sys


# def string_validation(input) -> bool:
#     """
#     Checks a validation of string from a command-line argument
#     """
#     if any(not input.isdigit() and not input.isalpha() and not input.isspace()):
        


def execute_filter():
    """
    Filters a list of words based on their length.

    This function:
    - Uses a filtering function (`ft_filter`) to select words
    longer than the given length.
    - Prints the filtered words as a list.
    """

    if len(sys.argv) != 3:
        raise AssertionError(": the arguments are bad")
    if sys.argv[1].isnumeric():
        raise AssertionError(": the arguments are bad")
    if not all(char.isalnum() or char.isspace() for char in sys.argv[1]):
        raise AssertionError(": invalid character")
    
    words = list(sys.argv[1].split(' '))
    result = ft_filter(lambda x: len(x) > int(sys.argv[2]), words)
    printed_res = [res for res in result]
    print(printed_res)


def main():
    """
    Main function to execute the word filtering script.
    """

    try:
        execute_filter()
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
