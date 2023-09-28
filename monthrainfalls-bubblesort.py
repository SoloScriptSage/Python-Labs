# Vladyslav Hirchuk
# Lab 7

# Declare string array for months
months = ["January", "February", "March", 
     "April", "May", "June", "July", 
     "August", "September", "October",
     "November", "December"]

# Declare string array for amount of rainfalls each month
rainfalls = []

for i in range(12):
    # Prompring the amount of rainfalls each month and appending them in array
    each_rainfalls_amount = int(input(f"Please enter the rainfall for {months[i]}: "))
    rainfalls.append(each_rainfalls_amount)

# Declare a variable for amount of rainfalls (12)
rainfalls_amount = len(rainfalls)

# BubbleSort
for i in range(rainfalls_amount-1):
    # weSwapped is a boolean which is going to make code faster in case if all array is sorted
    weSwapped = False
    for j in range(0, rainfalls_amount-i-1):
        # Comparing all the numbers in array and swapping in case if the first number is bigger than the second one
        if rainfalls[j] > rainfalls[j+1]:
            # If we swapped than the boolean weSwapped is True
            weSwapped = True
            # Swap numbers and month in array
            rainfalls[j], rainfalls[j+1] = rainfalls[j+1], rainfalls[j]
            months[j], months[j+1] = months[j+1], months[j]
    if not weSwapped:
        break

print("Here are the sorted rainfall totals:")

# Display the results
for i in range(rainfalls_amount):
    print(f"{months[i]}: {rainfalls[i]}")
