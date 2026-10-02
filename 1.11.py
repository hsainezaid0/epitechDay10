def my_count(stop, start=0, step=1):
    if type(stop) is not int:
        raise ValueError("stop doit être un entier.")

    if type(start) is not int:
        raise ValueError("start doit être un entier.")

    if type(step) is not int:
        raise ValueError("step doit être un entier.")

    if step == 0:
        raise ValueError("step ne peut pas être égal à zéro.")

    for number in range(start, stop, step):
        print(number)


try:
    my_count(100, -100, 42)
except ValueError as error:
    print("Erreur :", error)
