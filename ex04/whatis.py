import sys

def determine_arg() :
    if len(sys.argv) > 2 :
        raise AssertionError(": more than one argument is provided")
    elif len(sys.argv) < 2:
        raise AssertionError(": less than one argument is provided")
    try :
        int(sys.argv[1])
    except:
        raise AssertionError("argument is not an integer ")
    if int(sys.argv[1]) % 2 == 0 :
        print("I'm Even")
    elif int(sys.argv[1]) % 2 == 1: 
        print("I'm Odd")

try:
    determine_arg()
except AssertionError as msg:
    print(f"AssertionError: {msg}")