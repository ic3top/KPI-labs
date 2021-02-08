while True:
    try:
        number = abs(int(input("number: ")))
        break
    except ValueError:
        continue
even = 0
odd = 0

while number > 0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number //= 10

print("Even:{0:_^3}, odd:{1:_^3}".format(even, odd))