# Fibonacci series
# User_Input= int(input("Insert the fibonacci number needed ",))
User= input("Insert the fibonacci number needed  ",)
while not User.isdigit():
    print("Kindly Input a Digit")
    User= input()
User_Input = int(User)
n= User_Input + 1
# n=10
Series= range(1,n)
a= 0
b = 1
Fib = [0, 1]
for i in Series:
     c= a + b
     Fib.append(c)
     a=b
     b=c
     
print(Fib)

