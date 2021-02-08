sum = float(input("Total credit: "))
n = float(input("period of credit using in years: "))
p = float((input("percent of bank per month (example: 20%): ").replace("%", ""))) / 100
m = round((sum * p * (1 + p)**n) / (12 * (((1 + p)**n) - 1)))
total_m = round(m * (n*12))
print(f"Paying per month: {m}\nTotal payment: {total_m}")

