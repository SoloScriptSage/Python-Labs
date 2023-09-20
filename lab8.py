# Lab 9 
# Hirchuk Vladyslav

# Function to display the menu options
def menu():
    print("1.  Calculate the number of uppercase characters")
    print("2.  Calculate the number of lowercase characters")
    print("3.  Calculate the number of numeric digits")
    print("4.  Calculate the number of whitespace characters")
    print("5.  Quit\n")

# Function to count the number of uppercase characters in a string
def count_uppercase_characters(s):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count

# Function to count the number of lowercase characters in a string
def count_lowercase_characters(s):
    count = 0
    for char in s:
        if char.islower():
            count += 1
    return count

# Function to count the number of numeric digits in a string
def count_numeric_digits(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count

# Function to count the number of whitespace characters (spaces, tabs, and newlines) in a string
def count_whitespace_characters(s):
    count = 0
    for char in s:
        if char.isspace():
            count += 1
    return count

# Main function to run the program
def main():
    while True:
        menu()
        choice = input("Choice: ")
        match choice:
            case "1":
                s = input("Enter the sentence: ")
                print(f"Uppercase letters amount: {count_uppercase_characters(s)}\n")
            case "2":
                s = input("Enter the sentence: ")
                print(f"Lowercase letters amount: {count_lowercase_characters(s)}\n")
            case "3":
                s = input("Enter the sentence: ")
                print(f"Numeric digits amount: {count_numeric_digits(s)}\n")
            case "4":
                s = input("Enter the sentence: ")
                print(f"Whitespace characters amount: {count_whitespace_characters(s)}\n")
            case "5":
                quit()
            case _:
                print("Invalid input. Please enter a number.")

# Call the main function to start the program
main()
