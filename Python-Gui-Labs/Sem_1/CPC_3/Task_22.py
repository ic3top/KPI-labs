# a + b> c, a + c> b, b + c> a, (a> 0, b> 0, c> 0)
print("Sides of the triangle:")
a = float(input("The biggest side: a = "))
b = float(input("b = "))
c = float(input("c = "))
if a > 0 and b > 0 and c > 0:
    if b + c > a or b + c == a:
        print("Exists!")
    else:
        print("Doesn`t exist")
else:
    print("Impossible length")

