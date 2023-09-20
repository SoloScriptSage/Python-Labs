#Vladyslav Hirchuk
#Assignment 3.1

#Asking for a price of the product
price = float(input("Please enter your item's price: "))

#Print Subtotal and tax
print("Your total is: ")
print("------------------------------------------")
print(f"Subtotal:\t", "%.2f" % price)
tax = round(price * 0.0625, 2)
print(f"Tax:\t\t", "%.2f" % tax)
print("------------------------------------------")

#Print Total price
total = price + tax
print(f"Total:\t\t", "%.2f" % total)
print("------------------------------------------")

#Would you like to tip?
while True:
    choice = str(input("Would you like to leave a tip? (y/n): "))
    choice = choice.lower()
    match choice:
        case "y":
            tip = round(float(input("How much would you like to tip? ")), 2)
            print("------------------------------------------")
            print(f"Tip:\t\t", "%.2f" % tip)
            total += tip
            print(f"New Total:\t", "%.2f" % total)
            print("------------------------------------------")
            break
        case "n":
            print("OK. Have a nice day!")
            break
        case _:
            continue

