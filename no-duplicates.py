
class Node:
	def __init__(self, data=None):
		self.data = data
		self.next_node = None

class LinkedList:
	def __init__(self):
		self.head = None

	def add_node(self, data):
		if self.contains(data):
			print(f"Duplicate value {data} not added.")
			return

		new_node = Node(data)
		if not self.head:
			self.head = new_node
		else:
			current_node = self.head
			while current_node.next_node:
				current_node=current_node.next_node
			current_node.next_node = new_node

	def contains(self, data):
		current_node = self.head
		while current_node:
			if current_node.data == data:
				return True
			current_node = current_node.next_node
		return False

	def display_list(self):
		current_node = self.head
		while current_node:
			print(current_node.data, end=" -> ")
			current_node = current_node.next_node
		print("None")

def __add_value__(myLinkedList):
	value = input("Enter the value to add: ")
	myLinkedList.add_node(value)

def __display_all_values__(myLinkedList):
	myLinkedList.display_list()

def __exit_program__(myLinkedList):
	print(f"Exiting the program.")
	exit()

def main():
    myLinkedList = LinkedList()

    while True:
        print("\nMenu:")
        print("1. Add a value")
        print("2. Display all values")
        print("3. Exit")
        c = int(input("Enter your choice (1/2/3): "))
        match c:
            case 1:
                __add_value__(myLinkedList)
            case 2:
                __display_all_values__(myLinkedList)
            case 3:
                __exit_program__(myLinkedList)

if __name__ == "__main__":
    main()
