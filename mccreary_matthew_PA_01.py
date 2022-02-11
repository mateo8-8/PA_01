
rad = int(input("Enter a length for the radius: "))

if (rad < 0):
    print("ERROR: Input cannot be negative.")
    exit
else:
    area = 3.14159 * (rad * rad)
    perimeter = 2 * 3.14159 * rad
    print("Area is: ", area)
    print("Perimeter is: ", perimeter)
