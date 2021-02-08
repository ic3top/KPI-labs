import math
h = float(input("The height: "))
r = float(input("The diameter: "))/2
s_paint = float(input("Аrea that can be painted with paint from one jar: "))
s = 2*math.pi*r*(h+r)
jars = math.ceil(s/s_paint)
print(f"You need {jars} jars of paint")

