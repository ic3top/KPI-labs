number = int(input("Your number: "))

d1 = number % 10
d2 = number % 100 // 10
d3 = number // 100

print(f"The sum of the digits of a number: {d1 + d2 + d3:_^10}")
