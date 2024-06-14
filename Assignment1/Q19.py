# Write a python program that removes all punctuation from a given string.

str=input("Enter string :")
finalstr=""
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in str:
    if i not in punc:
        finalstr+=i
print("After removing all punctuation from a given string=",finalstr)