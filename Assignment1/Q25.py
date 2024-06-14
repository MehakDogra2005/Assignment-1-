# Write a program that copies the contents of one text file to another.
content=" "
with open("practice.txt", "r") as f:
    content = f.read()
with open("Copied.txt", "w") as copied:
    copied.write(content)

print("Successfully executed")