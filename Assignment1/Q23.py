# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
print("Enter F to convert the temperature in Fahrenheit and C to convert the temperature in Celsius")
choice= input()

if (choice == 'F'):
    c_1 = int(input("Enter temperature in celsius "))
    f_1 = 9/5 * c_1 + 32
    print(c_1 ,"C in fahrenheit = ",f_1 ,"F")
else:
    f_2 = int(input("Enter temperature in fahrenheit "))
    c_2 = (f_2 - 32) / 1.8
    print(f_2 ," F in celsius = ",c_2 ,"C")
