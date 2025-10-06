# Define age
age = 2007

# Take user input
year = int(input("Enter the year you were born: "))

# Check if it's a leap year
if year % 4 == 0:
    print("You were born in a leap year")
else:
    print("You were not born in a leap year")

# Compare ages
if age > year:
    print("You are older than me.")
elif age < year:
    print("You are younger than me.")
elif age == year:
    print("You are the same age as me.")