import math
def lcm(a, b):
    return (a * b) // math.gcd(a, b)


while True:
    try:
        x = int(input('a = '))
        y = int(input('b = '))
        print('Результат\nН.С.К. :', lcm(x, y))
    except ValueError:
        break