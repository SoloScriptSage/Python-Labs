# Global variable for the total cost of the paint job
total = 0

# Main method
def main():
    wallSpace = float(input("Enter the square feet of wall space: "))
    paintPrice = float(input("Enter the price of the paint per gallon: "))

    total = paint(wallSpace, paintPrice)

    print(f"The total cost of the paint job is: {total}")

# Method for determining the amount and cost of paint
def paint(wall_space, paint_price):
    amountOfGallons = wall_space / 115
    costOfPaint = amountOfGallons * paint_price

    print(f"The number of gallons of paint required: {amountOfGallons}")
    print(f"The cost of the paint: {costOfPaint}")

    costOfPaint += labor(amountOfGallons)

    return costOfPaint

# Method for determining the amount and cost of the labor
def labor(amount_of_gallons):
    hoursOfLabor = amount_of_gallons * 8
    costOfLabor = hoursOfLabor * 20.00

    print(f"The hours of labor required: {hoursOfLabor}")
    print(f"The labor charges: {costOfLabor}")

    return costOfLabor

# Main method to start the program
main()
