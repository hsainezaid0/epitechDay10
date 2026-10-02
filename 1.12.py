def new_division(num, den, acc=1):
    if type(num) not in (int, float):
        raise ValueError("num doit être un nombre.")

    if type(den) not in (int, float):
        raise ValueError("den doit être un nombre.")

    if den == 0:
        raise ValueError("Impossible de diviser par zéro.")

    if type(acc) is not int or acc < 0:
        raise ValueError("acc doit être un entier positif ou nul.")

    result = num / den

    print(f"{result:.{acc}f}")


try:
    new_division(8.4, 13)
    new_division(8.4, 13, 6)
except ValueError as error:
    print("Erreur :", error)
