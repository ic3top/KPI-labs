import re
mult = 1
number = input("Your number: ")
regex = r"(^0{1,})"  # starts on 0
regex2 = r"(0{1,}$)"  # ends on 0
regex3 = r"(^0{1,}\.?,?0{0,})"  # 0 before `,` or `.` and after
# if number is float
if number.find(".") != -1 or number.find(",") != -1:
    number = number.replace(",", "").replace(".", "")
    number = int(re.sub(regex3, "", number, 1))
# if number is int
else:
    number = re.sub(regex, "", number, 1)
    number = int(re.sub(regex2, "", number, 1))
print(number)
# multiplying all digits
while number > 0:
    digit = number % 10
    mult = mult * digit
    number = number // 10

print(f"RESULT:{mult:_^10}")