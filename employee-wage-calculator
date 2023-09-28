# Lab 6
# Hirchuk Vladyslav

# Declare an integer array to hold employee identification numbers
empId = [56588, 45201, 78951, 87775, 84512, 13028, 75804]

# Declare an integer array to hold the number of hours worked by each employee
hours = [0] * 7

# Declare an array of seven Reals to hold each employee’s hourly pay rate
payRate = [0.0] * 7

# Declare an array of seven Reals to hold each employee’s gross wages
wages = [0.0] * 7

# Propmt the user for hours and pay rate
for i in range(0, 7):
    hours[i] = float(input(f"Enter the hours for employee {empId[i]}: "))
    payRate[i] = float(input(f"Enter the pay rate for employee {empId[i]}: "))

    # Calculate the wages (hours times pay rate)
    wages[i] = hours[i] * payRate[i]

# Display the employee ID numbers and wages
print(f"\n\nEmployee ID\tWages")
print(f"===========================")

for i in range(0, 7):
    print(f"{empId[i]}\t\t${format(wages[i], '.2f')}")
