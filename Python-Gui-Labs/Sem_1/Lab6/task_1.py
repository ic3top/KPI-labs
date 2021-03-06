class Planet(object):
    def __init__(self, name, num, dist, volume, mas, speed):
        self.name = name
        self.num = num
        self.dist = dist
        self.volume = volume
        self.mas = mas
        self.speed = speed

    def density(self):
        return round(self.mas/self.volume/10**12, 3)  # gr/cm^3

    def mass_div(self):
        return round(5.97219 * 10 ** 24 / self.mas, 3)

    def speed_div(self):
        return round(29.8 / self.speed, 3)


# (distance in km, volume in km^3, mass in kg, speed in km/s)
Mercury = Planet("Mercury", 1, 579 * 10 ** 5, 6.083 * 10 ** 10, 0.32868 * 10 ** 24, 47.8)
Venus = Planet("Venus", 2, 1082 * 10 ** 5, 69.38 * 10 ** 11, 4.868 * 10 ** 24, 35)
Earth = Planet("Earth", 3, 1496 * 10 ** 5, 1.083 * 10 ** 12, 5.976 * 10 ** 24, 29.7)
Mars = Planet("Mars", 4, 2279 * 10 ** 5, 1.6318 * 10 ** 11, 0.64171 * 10 ** 24, 24.1)
Jupiter = Planet("Jupiter", 5, 7785 * 10 ** 5, 1.4313 * 10 ** 15, 1.89813 * 10 ** 27, 13.06)
Saturn = Planet("Saturn", 6, 1430 * 10 ** 6, 8.2713 * 10 ** 14, 5.6846 * 10 ** 26, 9.69)
Uranus = Planet("Uranus", 7, 2871 * 10 ** 6, 6.833 * 10 ** 13, 8.6 * 10 ** 25, 6.81)
Neptune = Planet("Neptune", 8, 4497 * 10 ** 6, 6.254 * 10 ** 13, 1.0243 * 10 ** 26, 5.43)

planets_lst = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]

while True:
    pln = input("Type name of the planet, 'exit' or 'list': ").capitalize()
    if pln == "Exit":
        break
    elif pln == "List":
        planets_lst.sort(key=lambda x: x.density())
        for x in planets_lst:
            print(f'Planet number - {x.num}, density - {x.density()} (g/cm^3) and orbital speed - {x.speed_div()}', end="\n"+("-"*40)+"\n")
    else:
        for x in planets_lst:
            if pln == x.name:
                if x.name == "Earth":
                    print(('\nPlanet: {0:_^20}\nIts` density ~ {1} (grams per centimeter^3)\n'+("-"*40)).format(x.name, x.density()))
                else:
                    print('\nPlanet: {0:_^20}\nIts` density ~ {1} (grams per centimeter^3)\n\
The ratio of the mass of the earth to the mass of {0} ~ {2}\n\
The ratio of the orbital speed of the Earth to the orbital speed of {0} ~ {3}\n'.format(x.name, x.density(), x.mass_div(), x.speed_div()), end=("-"*40+"\n"))
            else:
                continue
