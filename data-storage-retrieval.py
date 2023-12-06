class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class CollectionManager:
    def __init__(self):
        self.collection = []

    def add_contact(self, contact):
        self.collection.append(contact)
        print(f"Contact {contact.name} added to the contact list.")

    def delete_contact(self, name):
        for contact in self.collection:
            if contact.name == name:
                self.collection.remove(contact)
                print(f"Contact '{name}' deleted from the contact list.")
                return
        print(f"Contact '{name}' not found in the contact list.")

    def display_collection(self):
        if not self.collection:
            print("The contact list is empty.")
            return

        header = "+----------------------+----------------------+--------------------------+"
        row_format = "|{:<22}|{:<22}|{:<26}|"
        print(header)
        print(row_format.format("Name", "Phone number", "Email"))
        print(header)

        for contact in self.collection:
            print(row_format.format(contact.name, contact.phone, contact.email))

        print(header)

    # Bubble sort ascending sorting by name
    def bubble_sort_ascending(self):
        arr = self.collection.copy()
        n = len(arr)

        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j].name > arr[j+1].name:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr

    # Bubble sort descending sorting by name
    def bubble_sort_descending(self):
        arr = self.collection.copy()
        n = len(arr)

        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j].name < arr[j+1].name:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr

def main():
    contact_list = CollectionManager()

    test1 = Contact("John Doe", "555-1234", "john.doe@example.com")
    test2 = Contact("Jane Smith", "555-5678", "jane.smith@example.com")
    test3 = Contact("Alice Johnson", "777-4321", "alice.johnson@example.com")
    test4 = Contact("Bob Williams", "999-8765", "bob.williams@example.com")

    contact_list.add_contact(test1)
    contact_list.add_contact(test2)
    contact_list.add_contact(test3)
    contact_list.add_contact(test4)



    sorted_contacts_ascending = contact_list.bubble_sort_ascending()
    contact_list.display_collection(sorted_contacts_ascending)

    sorted_contacts_descending = contact_list.bubble_sort_descending()
    contact_list.display_collection(sorted_contacts_descending)

    while True:
        print("\nMenu:")
        print("1. Add new contact")
        print("2. Delete contact")
        print("3. Display contact list")
        print("4. Sort in ascending order")
        print("5. Sort in descending order")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        match choice:
            case '1':
                add_contact()
            case '2':
                delete_contact()
            case '3':
                display_collection()
            case '4':
                sort_ascending()
            case '5':
                sort_descending()
            case '6':
                quit_program()
            case _:
                print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
