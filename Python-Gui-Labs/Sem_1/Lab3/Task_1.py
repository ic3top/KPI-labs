str1 = list(input("First string: ").replace(" ", ""))
str2 = list(input("Second with the same length: ").replace(" ", ""))

# checking for the equal length
if len(str1) != len(str2):
    if len(str1) < len(str2):
        while len(str1) < len(str2):
            str1.append("0")
    else:
        while len(str1) > len(str2):
            str2.append("0")

# adding str1 list to the result
result = []
result.extend(str1)

# inserting into result elements from str2 with odd indexes
index = 1
for i in list(str2):
    result.insert(index, i)
    index += 2

print("Result: {}".format("".join(result).center(10)))
