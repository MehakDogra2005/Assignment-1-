# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

str=input("Enter string :")
finalstr=""
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in str:
    if i not in punc:
        finalstr+=i
print("After removing all punctuation from a given string=",finalstr)