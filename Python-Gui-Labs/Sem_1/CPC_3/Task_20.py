import random
left = round(float(input("Left border:  ")))
right = round(float(input("right border: ")))
print(random.randint(left, right))
print(f"{random.uniform(left, right):.1f}")
