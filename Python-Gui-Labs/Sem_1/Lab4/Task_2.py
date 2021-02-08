import random
product = 1
min_row_numbers = []
m, n = int(input('Amount of rows: ')), int(input('and amount of columns: '))

matrix = [[random.randrange(1, 1001) for y in range(n)] for x in range(m)]
for row in matrix:
    min_row_numbers.append(min(row))
    product *= min(row)

print("Randomly created matrix:\n", str(matrix).replace("],", "\n"))
print(f"""Minimal numbers from every row of matrix: {min_row_numbers}
and their product: {product}""")

