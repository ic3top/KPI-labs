solar_system = {
    "Mercury": (579 * 10 ** 5, 6.083 * 10 ** 10, 47.8),  # (distance in km, volume in km, speed in km/s)
    "Venus": (1082 * 10 ** 5, 9.38 * 10 ** 11, 35),
    "Earth": (1496 * 10 ** 5, 1.083 * 10 ** 12, 29.7),
    "Mars": (2279 * 10 ** 5, 1.6318 * 10 ** 11, 24.1),
    "Jupiter": (7785 * 10 ** 5, 1.4313 * 10 ** 15, 13.06),
    "Saturn": (1430 * 10 ** 6, 	8.2713 * 10 ** 14, 9.69),
    "Uranus": (2871 * 10 ** 6, 6.833 * 10 ** 13, 6.81),
    "Neptune": (4497 * 10 ** 6, 6.254 * 10 ** 13, 5.43),
}


def sorter(num, rev=True, main=solar_system):
    lst = list(main.items())
    print(type(lst[0]))
    lst.sort(key=lambda i: i[1][num], reverse=rev)
    for a in lst:
        if a[1][num] < 1000:
            print(a[0] + ': ' + str(a[1][num]), end=" km/s\n")
        else:
            print(a[0] + ': ' + str(a[1][num]), end=" km\n")


print("Distance from sun (grater -> smaller):")
sorter(0)
print("\nVolume of the planets (smaller -> grater) in km^3:")
sorter(1, False)
print("\nSpeed from (grater -> smaller):")
sorter(2)
