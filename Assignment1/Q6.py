# Write a program that reads the content of a text file and prints it to the console.

with open("practice.txt", "r") as f:
    content = f.read()
print(content)
print("Successfully executed")