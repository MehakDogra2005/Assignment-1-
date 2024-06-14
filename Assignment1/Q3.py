#Write a python program that calculates the factorial of a given number.
num = int(input("Enter number = "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("Fctorial of",num,"=",fact)
