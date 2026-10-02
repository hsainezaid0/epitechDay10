def check_even(number):
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(check_even, numbers))

print(even_numbers)
