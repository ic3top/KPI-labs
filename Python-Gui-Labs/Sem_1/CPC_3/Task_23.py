# a + b> c, a + c> b, b + c> a, (a> 0, b> 0, c> 0)
print("Sides of the triangle:")
a = float(input("biggest side of the triangle - a = "))
b = float(input("b = "))
c = float(input("c = "))
if a > 0 and b > 0 and c > 0:
    if b + c > a:
        print("Exists!")
    elif b + c == a:
        print("The triangle exists and it`s also a degenerate triangle")
    else:
        if b + c < a:
            print(f"a + b < c ({c+b}<{a})")
else:
    print("One of the sides is less than zero")
