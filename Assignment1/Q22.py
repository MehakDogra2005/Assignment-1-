# Write a python program that returns the minimum and maximum values in a list of numbers
list1 =[1,2,5,6,8,9,0,5,56,87,90,100,34,5,-2]

min = list1[0]
max = list1[0]

for i in list1:
    if(i< min):
        min = i
    if (i>max):
        max=i
print("Maximum number in list =",max)
print("Minimum number in list =",min)
