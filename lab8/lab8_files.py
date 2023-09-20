
golfers = int(input("How many golfers will be entered: "))

outfile = open('golf.txt')
outfile.write("Golfer's name\t|\tScore")

for i in range(golfers):
    name = input(f"{i}. Golfer's name: ")
    score = input(f"{i}. Golf score: ")

    outfile.write(f"{i}. {name}\t{score}")

    


