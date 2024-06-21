import sys
import string

def count_characters(text):
    """
    Count different types of characters in the given text.

    Parameters:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with counts for upper-case letters, lower-case letters,
              punctuation characters, digits, and spaces.
    """
    counts = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "digits": 0,
        "spaces": 0
    }

    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char in string.punctuation:
            counts["punctuation"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        elif char.isspace():
            counts["spaces"] += 1

    return counts

def main():
    """
    Main function to handle command-line arguments and count character types in the provided text.
    """
    if len(sys.argv) > 2:
        raise AssertionError("More than one argument is provided")
    
    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("Please provide a string: ")

    counts = count_characters(text)
    total_chars = len(text)

    print(f"The text contains {total_chars} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")

if __name__ == "__main__":
    """
    Entry point of the script. Handles command-line argument parsing and calls the main function.
    """
    main()
