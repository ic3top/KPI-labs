n = int(input("Number: "))
s, i = 0, 0

while s <= n:
    i += 1
    s += 1/i

# Results
print("Last number was: 1/{}". format(i))
print("Total: ", s)
