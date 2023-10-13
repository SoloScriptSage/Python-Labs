

def showmenu():
    print("1. Selection-sort") # searching for lowest and swapping lowest index with num we found
    print("2. Insertion-sort")
    print("3. Merge-sort")
    print("4. Quick-sort")
    print("5. Bubble-sort")
    print("6. Exit")

#selection-sort
def find_smallest(values, start):
    value = values[start]
    index = start
    for i in range(start, len(values)):
        if values[i] < value:
            value = values[i]
            index = i
    return index

def selection_sort():
    values = [3, 5, 7, 2, 1, 8, 4, 6, 9]

    for unsorted in range(len(values)):
        print(values)
        smallIndex = find_smallest(values, unsorted)
        temp = values[unsorted]
        values[unsorted] = values[smallIndex]
        values[smallIndex] = temp

#insertion-sort
def insertion_sort():
    values = [3, 5, 7, 2, 1, 8, 4, 6, 9]

    for unsorted in range(1, len(values)):
        valueToInsert = values[unsorted]

        index = 0
        while values[index] < valueToInsert:
            index += 1

        values.remove(valueToInsert)
        values.insert(index, valueToInsert)

#merge-sort
values = [3, 5, 7, 2, 1, 8, 4, 6, 9]

def merge(values, begin, mid, end):
    temp = []
    tempind = 0

    ind1 = begin
    ind2 = mid+1

    size = end - begin + 1  # Corrected the size calculation
    for tempind in range(size):
        if ind1 <= mid and ind2 <= end:
            if values[ind1] < values[ind2]:
                temp.append(values[ind1])
                ind1 += 1
            else:
                temp.append(values[ind2])
                ind2 += 1
        elif ind1 <= mid:
            temp.append(values[ind1])
            ind1 += 1
        else:
            temp.append(values[ind2])
            ind2 += 1

    values[begin:end + 1] = temp

def merge_sort(values, begin, end):
    if begin < end:
        mid = (begin + end) // 2
        merge_sort(values, begin, mid)
        merge_sort(values, mid, end)

        merge(values, begin, mid, end)

def quick_sort():
    print("metge")
def bubble_sort():
    print("metge")

def main():
    while True:
        showmenu()
        choice = str(input("Which sorting algorithm you want to use? "))

        match choice:
            case "1":
                selection_sort()
            case "2":
                insertion_sort()
            case "3":
                merge_sort()
            case "4":
                quick_sort()
            case "5":
                bubble_sort()
            case "6":
                exit()
            case _:
                continue

main()
