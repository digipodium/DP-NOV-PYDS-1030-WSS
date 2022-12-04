a = input("Enter a number: ")
b = input("Enter another number: ")
if a.isnumeric() and b.isnumeric():
    a,b = int(a),int(b)
    c = a + b
    print("The sum of the numbers is: ", c)
else:
    print("Please enter numbers only")