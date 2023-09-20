#Vladyslav Hirchuk
#Assignment 3.2

num = int(input("How many bottles? Please enter an integer: "))

while num > 0: 
    print(f"{num} bottles of water on the wall, {num} bottles of water!")
    num -= 1
    print(f"Take one down, pass it around, {num} bottles of water!")

print("Done!")
