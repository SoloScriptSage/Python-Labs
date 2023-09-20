# Lab 8
# Hirchuk Vladyslav

golfers = int(input("How many golfers will be entered: "))

with open('golf.txt', 'w') as outfile:
    outfile.write("Golfer's name\t|\tScore\n")

    for i in range(golfers):
        name = input(f"{i+1}. Golfer's name: ")  # Changed i to i+1 for a more user-friendly display
        score = input(f"{i+1}. Golf score: ")

        outfile.write(f"{i+1}. {name} \t\t {score}\n")  # Added '|' to separate the name and score

print("Done!")
