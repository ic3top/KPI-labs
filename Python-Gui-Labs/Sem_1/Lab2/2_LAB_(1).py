import math
x, y = None, None
# Making sure that user inputs X as a number
while x is None:
    try:
        x = float(input("value of x: "))
    except ValueError:
        print("Value ERROR detected! \nX must be an integer")
# Making sure that user inputs Y as a number
while y is None:
    try:
        y = float(input("value of y: "))
    except ValueError:
        print("Value ERROR detected! \n Y must be an integer")

# result calculating if while blocks were passed
result = (2.37 * math.sin(x+1)) / (math.sqrt(4 * y ** 2 - 0.1 * y + 5))
print("Result:", result)
