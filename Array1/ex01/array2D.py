import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
        takes as parameter a 2D array,
        print its shape, return a truncated version of the array based
        on the provided start and end arguments.
        using slicing method.
    """
    try:
        if not isinstance(family, list) \
                or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Input must be a list and 2 integers.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Input list with different sizes.")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end+1].shape}")
        return np.array(family)[start:end].tolist()
    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
        return ""
    
def main():
    family = [[1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

if __name__ == "__main__":
    main()
