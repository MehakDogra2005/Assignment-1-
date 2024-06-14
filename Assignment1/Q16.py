# Write a program in python that counts the frequency of each character in a string.

str = input("Enter ")
char_frequency={}

for char in str:
    if (char in char_frequency):
        char_frequency[char]= char_frequency[char]+1
    else:
        char_frequency[char]=1
print(char_frequency.items())