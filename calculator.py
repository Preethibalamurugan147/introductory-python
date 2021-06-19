print('Please enter first number')
a = int(input())
print('Please enter second number')
b = int(input())
print('if adddition is required press + \n if multiplication is required press *')
print('if subtraction is required press - \n if division is required press / ')
operator = input()
if operator == "+":
    print(a+b)
elif operator == "*":
    print(a*b)
elif operator == "-":
    print(a-b)
elif operator == "/":
    print(a/b)
else:
    print("operation invalid")
