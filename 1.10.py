def my_count(stop, start=0):
    if type(stop) is not int or type(start) is not int:
        raise ValueError("start et stop doivent être des entiers.")

    if start <= stop:
        step = 1
    else:
        step = -1

    for number in range(start, stop + step, step):
        print(number)


my_count(5)
