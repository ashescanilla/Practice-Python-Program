# Program that ask user to input 10 numbers. Print how many are odd numbers.


count = 0
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 != 0:
        count += 1

print("Number of odd numbers:", count)