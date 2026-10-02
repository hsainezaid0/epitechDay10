def my_division(num, den):
    if type(num) is not int or type(den) is not int:
        raise ValueError("Les deux arguments doivent être des entiers.")

    if den == 0:
        raise ValueError("Impossible de diviser par zéro.")

    quotient = num // abs(den)
    remainder = num % abs(den)

    if den < 0:
        quotient = -quotient

    return quotient, remainder


try:
    quotient, remainder = my_division(42, 4)

    print(quotient)
    print(remainder)

except ValueError as error:
    print("Erreur :", error)
