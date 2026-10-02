def ship(*names, **address):
    for name in names:
        print(name, end=" ")

    print()

    for key in address:
        print(key, ":", address[key])


ship("Batman", street="Mountain Drive", city="Gotham")
