# Write a python program that counts the occurrences of a specific element in a list

key = 9
list1 = [1,4,9,9,7,8,9,4,9,5,6,5]
count = 0

for i in list1:
    if(key == i) :
        count = count +1
print("Number of times 9 is found = ",count)