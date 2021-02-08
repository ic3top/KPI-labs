import random
res = []
while len(res) < 5:
    res.append(round(random.random() * random.randrange(0, 10000, 10)))
res = tuple(res)
print(res)
