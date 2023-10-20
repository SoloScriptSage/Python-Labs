
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.dummynode = Node(None)

    def isEmpty(self):
        return self.dummynode.next == None

    def display(self):
        temp = self.dummynode.next
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def addFront(self, value):
        newNode = Node(value)
        newNode.next = self.dummynode.next
        self.dummynode.next = newNode

    def addBack(self, value):
        temp = self.dummynode

        while temp.next != None:
            temp=temp.next

        temp.next = Node(value)

    def removeFront(self):
        temp = self.dummynode
        self.dummynode.next = temp.next
        temp.next = None

    def removeBack(self):
        temp = self.dummynode.next
        trailer = self.dummynode

        while temp.next != None:
            temp = temp.next
            trailer = trailer.next

        trailer.next = None

    def search(self, key):
        temp = self.dummynode.next

        while temp != None:
            if temp.data == key:
                return temp
            temp = temp.next
        return None

    def remove(self, value):
        trailer = self.dummynode
        temp = trailer.next

        while temp != None and temp.data != value:
            temp = temp.next
            trailer = trailer.next

        if temp != None:
            trailer.next = temp.next
            temp.next = None

    def count(self):
        counter = 0
        temp = self.dummynode.next

        while temp != None:
            counter += 1
            temp = temp.next

        return counter

def show_menu():
    print("Linked List Menu:")
    print("1. Display the linked list")
    print("2. Add to the front")
    print("3. Add to the back")
    print("4. Remove from the front")
    print("5. Remove from the back")
    print("6. Search for a value")
    print("7. Remove a value")
    print("8. Count the number of elements")
    print("9. Exit")

linked_list = LinkedList()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            linked_list.display()
        case "2":
            value = input("Enter a value to add to the front: ")
            linked_list.addFront(value)
        case "3":
            value = input("Enter a value to add to the back: ")
            linked_list.addBack(value)
        case "4":
            linked_list.removeFront()
        case "5":
            linked_list.removeBack()
        case "6":
            value = input("Enter a value to search for: ")
            linked_list.search(value)
        case "7":
            value = input("Enter a value to remove: ")
            linked_list.remove(value)
        case "8":
            linked_list.count()
        case "9":
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again.")
