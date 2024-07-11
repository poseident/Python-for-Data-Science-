import sys

def whatis():
    # Check if the number of arguments is not exactly one
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        return

    arg = sys.argv[1]

    # Validate the argument type
    try:
        number = int(arg)
    except ValueError:
        raise AssertionError("argument is not an integer")

    # Check if the number is even or odd
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    whatis()