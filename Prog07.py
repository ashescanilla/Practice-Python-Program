# Program that ask user to input 10 numbers. Print the sum of all the numbers.

numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
print("The sum of all numbers is:", total)