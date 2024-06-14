# Write a program that takes a string input from the user and writes it to a text file

str = input("Enter ")

with open("practice.txt","w") as f:
    f.write(str)
print("Successfully executed")