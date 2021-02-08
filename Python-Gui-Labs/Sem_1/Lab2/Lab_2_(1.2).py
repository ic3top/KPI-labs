import math
x, y = float(input("Value of x: ")), float(input("Value of y: "))

# result calculating
result = (2.37 * math.sin(x+1)) / (math.sqrt(4 * y ** 2 - 0.1 * y + 5))
print("Result:", result)

