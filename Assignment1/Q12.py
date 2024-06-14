# Write a python program that calculates the sum of the digits of a given number
num = int(input("Enter number = "))
sum = 0
while(num>0):
    sum = sum + num%10
    num=num//10
print("Sum of digits = ",sum)
    