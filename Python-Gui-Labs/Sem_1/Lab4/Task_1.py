import numpy as np
rm_lst = list(np.random.randint(-100, 100, 100))
odd = 0
even = 0
i = 1
new_lst = []

for num in rm_lst:
    if num % 2 == 0 and num > even:
        even = num
    elif num % 2 != 0 and num > odd:
        odd = num

# difference between even and odd number in module(abs)
difference = abs(even - odd)
# value of closest number to the "difference" in rm_tuple + deleting this number from rm_tuple => len(rm_tuple) = 98
closest_num = rm_lst.pop(rm_lst.index(min(rm_lst, key=lambda x: abs(x - difference))))

while i < len(rm_lst):
    if closest_num + rm_lst[i] > 10:
        new_lst.append(rm_lst[i])
    i += 1
# result output
print(f"""Randomly created list: {rm_lst}
Value of greatest odd number: {odd}\tvalue of greatest even number: {even}\tand their difference: {difference}
Closest number to the difference: {closest_num}
Created new list: {new_lst}""")
