# First triangle
print("-" * 5 + " Sides of first triangle " + 5 * "-")
a1, b1, c1 = float(input("First side = ",)), float(input("Second side = ",)), float(input("Third side = ",))

# Geron`s Formula
p1 = (a1 + b1 + c1) / 2
s1 = ((p1 * (p1 - a1) * (p1 - b1) * (p1 - c1)) ** 0.5)

# second Triangle
print("-" * 5 + " Sides of Second triangle " + 5 * "-")
a2, b2, c2 = float(input("First side = ",)), float(input("Second side = ",)), float(input("Third side = ",))

p2 = (a2 + b2 + c2) / 2
s2 = ((p2 * (p2 - a2) * (p2 - b2) * (p2 - c2)) ** 0.5)

# result - output
if s1 > s2:
    print("The square of FIRST triangle({}) is grater than the second one({})".format(s1, s2))
elif s1 < s2:
    print("The square of SECOND triangle({}) is grater than the first one({})".format(s2, s1))
else:
    print("The squares are equal: {} = {}".format(s1, s2))
