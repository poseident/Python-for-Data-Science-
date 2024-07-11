def give_bmi(heigth: list[int | float], weigth: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values based on given heights and weights.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List of calculated BMI values.
    """
    try:
        if len(heigth) != len(weigth):
            raise ValueError("Lists of heigth and weigth must be provided.")
        bmi_values = []
        for h, w in zip(heigth, weigth):
            if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
                raise TypeError("Heigth and weigth must be integers or floats.")
            if h <= 0 or w <= 0:
                raise ValueError("Heigth and weigth values must be positive.")
            bmi = w / (h ** 2)
            bmi_values.append(bmi)
        return bmi_values
    except Exception as error:
        print("An error occured:", error)
        return []

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determine whether BMI values are above a given limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): Limit to compare BMI values against.

    Returns:
        list[bool]: List of booleans indicating whether
        each BMI value is above the limit.
    """
    if limit <= 0 or not isinstance(limit, int):
        raise ValueError("Limit must be at least 1and int")
    result = []
    for item in bmi:
        if not isinstance(item, (int, float)) or not isinstance(limit, int):
            raise TypeError("Heigth and weigth must be integers or floats.")
        if item > limit:
            result.append(True)
        else:
            result.append(False)
    return result

def main():
    height = [2.71, 1.15, 1.71, 1.15, 1.90]
    weight = [165.3, 38.4, 165.3, 80, 90.5]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

if __name__ == "__main__":
    main()