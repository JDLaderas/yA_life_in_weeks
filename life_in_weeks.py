age = int(input("Please enter your age: "))


yearsRemaining = 90 - age
days = yearsRemaining * 365
weeks = yearsRemaining *52
months = yearsRemaining * 12

calc = (f"your have {days} days, {weeks} weeks, {months} months")

print(calc)
