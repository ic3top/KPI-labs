import math

print("Input point`s coordinates and radius of circle")
x = float(input("x = "))
y = float(input("y = "))
r = float(input("R = "))

hypotenuse = math.sqrt(x ** 2 + y ** 2)

if hypotenuse <= r:
    print(f"The point M({x:.0f};{y:.0f}) belongs to the circle (r = {r:.0f})")
else:
    print(f"The point M({x};{y}) doesn`t belong to the circle (r = {r})")