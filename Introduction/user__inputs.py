numberOne = float(input("Enter a number\t"))
operator = input("Enter an operator\t")
numberTwo = float(input("Enter another number\t"))
result = 0

if operator == "+":
    result = numberOne + numberTwo
    print(result)
elif operator == "-":
    result = numberOne - numberTwo
    print(result)
elif operator == "*":
    result = numberOne * numberTwo
    print(result)
elif operator == "/":
    result = numberOne / numberTwo
    print(result)
else:
    print("Please enter a valid operator")

n = 99
print(type(n))