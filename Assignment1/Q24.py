# Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result
a = int(input("Enter number= "))
b = int(input("Enter number= "))
c = input("Enter opertor= ")

if(c=='+'):
    print(a+b)
elif(c=='-'):
    print(a-b)
elif(c=='*'):
    print(a*b)
elif(c=='/'):
    print(a/b)
elif(c=='%'):
    print(a%b)
elif(c=='**'):
    print(a**b)
else:
    print("Invalid operator")
