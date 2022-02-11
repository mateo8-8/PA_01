from tkinter import END


uInitial = input("Enter in a list of numbers, separated by a comma: ")
uSplit = uInitial.split(",")
#print(uSplit)
for x in uSplit:
    if x == '0':
        print("Error, you have entered 0, not valid value")
        break
