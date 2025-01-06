from ft_filter import ft_filter
import sys


def execute_filter():
    if len(sys.argv) != 3:
        raise AssertionError(": the arguments are bad")
    if sys.argv[1].isnumeric():
        raise AssertionError(": the arguments are bad")
    words = list(sys.argv[1].split(' '))
    result = ft_filter(lambda x: len(x) > int(sys.argv[2]), words)
    printed_res = [res for res in result]
    print(printed_res)


def main():
    try:
        execute_filter()
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()