# Take input
itemPrice = float(input("Enter the item price: "))

# Tax
itemTax = itemPrice*0.2

# Total price
totalPrice = itemPrice + itemTax 
print("Tax on the item is", itemTax)
amount = int(input("How many items do you want to buy?: s"))

# Multiply total by amount of items
totalPrice = totalPrice * amount

# Final printing
print("Total item price is", totalPrice)