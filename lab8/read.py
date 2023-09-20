# Lab 8
# Hirchuk Vladyslav

def read_info(filename):
    golf = []
    with open(filename, 'r') as infile:
        TITLE = infile.readline().strip()  # Read and store the header line
        for line in infile:
            index, data = line.strip().split('. ')
            name, score = data.split('\t\t')
            golf.append((name.strip(), score.strip()))
    return TITLE, golf

name_file = 'golf.txt'

try:
    TITLE, golf = read_info(name_file)

    print(f"{TITLE}")
    if len(golf) > 0:
        for i, (name, score) in enumerate(golf, start=1):
            print(f"{i}. {name} \t\t {score}")
    else:
        print("No data found in the file.")
except FileNotFoundError:
    print("The 'golf.txt' file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
