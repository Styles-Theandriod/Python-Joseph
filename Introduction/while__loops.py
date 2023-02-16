flag = True

while flag:
    numberOne = float(input("Enter a number\t"))
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
        flag = False
        print("Please enter a valid operator")


# SECOND EXAMPLE
# name = ""

# while name != "Gabby":
#     name = input("Please enter your name\t")
#     print(name)
#     if name == "Gabby":
#         print("Success!!")

