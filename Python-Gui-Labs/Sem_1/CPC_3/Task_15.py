print("Planet #1: ", end="")
r, speed = float(input("Planet`s radius(in km): ")), float(input("and it`s orbital speed (km/s): "))
print("Planet #2: ", end="")
r2, speed2 = float(input("Planet`s radius(in km): ")), float(input("and it`s orbital speed (km/s): "))
#  2 * радіус орбіти * π / орбітальна швидкість.
def count(radius, orbital_speed):
    a = ((2 * radius * 3.14) / orbital_speed)/(60*60*24)
    return a

year1 = count(r, speed)
year2 = count(r2, speed2)
if year1 > year2:
    print("The period of rotation around the sun on the first planet is longer")
else:
    print("The period of rotation around the sun on the second planet is longer")

print("The period of rotation around the sun №1: {:^10.0f} (in days on Earth)\n"
      "The period of rotation around the sun №2: {:^10.0f} (in days on Earth)".format(year1, year2))
