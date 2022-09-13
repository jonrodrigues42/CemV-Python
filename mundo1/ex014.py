# Convert celsius to fahrenheit / vice versa


def convert():
    print('1 - C to F\n2 - F to C')
    choic = input(':')
    if choic.isnumeric():
        choice = int(choic)
    else:
        print('Invalid, try agin...\n\n')
        convert()
    if choice == 1:
        print('C to F')
        c = float(input('Quantos graus Celcius? '))
        f = (c * (9 / 5)) + 32
        print('{:.2f}ºC é equivalente à {:.2f}ºF\n\n'.format(c, f))
        convert()
    if choice == 2:
        # (F − 32) × 5/9 = C
        print('F to C')
        f = float(input('Quantos graus F? '))
        c = (f - 32) * (5 / 9)
        print('{:.2f}F é equivalente à {:.2f}C\n\n'.format(f, c))
        convert()
    if choice > 2:
        print('Invalid, try again\n\n')
        convert()
    if choice < 1:
        print('Invalid, try again\n\n')
        convert()


convert()
