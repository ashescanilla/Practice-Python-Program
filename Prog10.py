# Program to print all numbers from 0 to 100 except those ending in zero

# Using a for loop to iterate through the range
for number in range(0, 101):  
    if number % 10 != 0:  
        print(number)  