sal = int(input("Enter your salary: "))
years = int(input("Enter the number of years you have worked here: "))

if sal < 200000 and years > 7:
    print("You are eligible for a bonus!")
    bBase = sal * .05
    sal = sal + bBase
    print("Your bonus is: $", bBase)
else:
    print("You are not eligible for a bonus yet")
