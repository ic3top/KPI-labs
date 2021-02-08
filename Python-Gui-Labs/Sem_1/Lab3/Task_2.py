res = bytearray(input("Write something: "), "UTF-8").replace(b"*", b"")
# copying same symbols, extending "res"
res.extend(res)
print("Your result: {}".format(res.decode("UTF-8").center(10)))
