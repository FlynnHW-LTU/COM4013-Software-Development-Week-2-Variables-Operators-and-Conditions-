print("Enter five different integers: ")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))

max_num = num1

if num2 > max_num:
    max_num = num2

if num3 > max_num:
    max_num = num3

if num4 > max_num:
    max_num = num4

if num5 > max_num:
    max_num = num5

print("The maximum number is:", max_num)