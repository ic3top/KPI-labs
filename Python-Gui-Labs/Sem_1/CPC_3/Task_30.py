def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


while True:
    try:
        x = int(input('a = '))
        y = int(input('b = '))
        print('Результат\nН.С.К. :', lcm(x, y))
    except ValueError:
        break
