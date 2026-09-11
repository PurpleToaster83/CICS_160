x = input("Enter the menu True/False?")
if 'true' in x.lower():
    print("In the menu!")
else:
    print("No menu for you")
print("done")

try:
    pass
except FileNotFoundError:
    pass