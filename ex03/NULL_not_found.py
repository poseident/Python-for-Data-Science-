def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} <class 'NoneType'>")
    elif isinstance(obj, float) and obj != obj:  # Checking for NaN
        print(f"Cheese: {obj} <class 'float'>")
    elif obj is False:
        print(f"Fake: {obj} <class 'bool'>")
    elif obj == 0:
        print(f"Zero: {obj} <class 'int'>")
    elif obj == '':
        print(f"Empty: <class 'str'>")
    else:
        print("Type not found")
        return 1
    return 0