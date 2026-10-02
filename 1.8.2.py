def my_sum(*numbers):
    total = 0

    for number in numbers:
        if type(number) not in (int, float):
            raise ValueError("Tous les arguments doivent être des nombres.")

        total += number

    print(total)
    return total


my_sum(1)
my_sum(1, 2, 3)
my_sum(-20, -10, 5, 5, 10, 10)

try:
    my_sum(1, "toto")
except ValueError as error:
    print("ValueError:", error)
