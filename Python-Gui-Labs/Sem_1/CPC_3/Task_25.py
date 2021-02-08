from math import sqrt

def fin(message):
    i = float(input(message))
    return i

while True:
    print("Square of circle - 1 | triangle - 2 | rectangle - 3 | exit - 0")
    answer = input("I choose: ")
    if answer == "circle" or answer == "1":
        r = fin("Radius of circle: ")
        s = r ** 2 * 3.14
        print(f"\nSquare of this circle\nS = {s:>3}")
        continue
    elif answer == "triangle" or answer == "2":
        print("\nWell, input all necessary data:")
        a = fin("a = ")
        b = fin("b = ")
        c = fin("c = ")

        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"S = {s:>3}")
        continue
    elif answer == "rectangle" or answer == "3":
        print("\nWell, input all necessary data:")
        a = fin("a = ")
        b = fin("b = ")
        s = a * b
        print(f"S = {s:>3}")
        continue
    elif answer == "exit" or answer == "0":
        break
