# Write a program that reads data from a CSV file and prints it to the console

import csv

file_name = input("Enter file name ")

with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)