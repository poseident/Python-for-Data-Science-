import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Exactly two arguments \
                (string and integer) are required.")
        
        text = sys.argv[1]
        n = int(sys.argv[2])

        if not isinstance(text, str) or not isinstance(n, int):
            raise AssertionError("Invalid argument types.")
        
        filtered_words = list(ft_filter(lambda word: len(word) > n, text.split()))

        print(filtered_words)

    except ValueError as error:
        print("ValueError:", error)
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()