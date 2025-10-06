celsius = float(input("Type in the celsius you want in fahrenheit: "))

# Function to convert
def celsiusToFahrenheit(celc):
    return(celc * (9/5) + 32)

# Set celsius to converted amount
celsius = celsiusToFahrenheit(celsius)

print(f"That is {celsius} Fahrenheit.")