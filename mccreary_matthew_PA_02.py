wide = int(input("Enter width value: "))
tall = int(input("Enter height value: "))

if wide < 0 or tall < 0:
    if wide < 0 and tall < 0:
        print("Error:  Both inputs are negative.")
    if wide < 0:
        print("Error: Width is negative")
    if tall < 0:
        print("Error:  Height is negatvie")
else:
    if wide == tall:
        print("This is a square")
    else:
        print("This is not a square")
