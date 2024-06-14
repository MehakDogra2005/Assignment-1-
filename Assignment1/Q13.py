# Write a program that asks the user for their birth year and calculates their age
Born= int(input("Enter year of birth = "))
presentYear= 2024
if(Born <0 or Born==0):
    print("Wrong year of birth")
else:
    print("Your age is", presentYear-Born)
