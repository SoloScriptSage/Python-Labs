#hirchuk-vladyslav

class_info = {
    "CIS1230": {
        "name": "Database Application",
        "instructor": "Liu, D",
        "schedule": "T 12:00 PM - 2:40 PM",
    },
    "CIS1410": {
        "name": "Intro Human Computer Interact",
        "instructor": "England, C",
        "schedule": "M 1:00 PM - 2:50 PM",
    },
    "CIS2532": {
        "name": "Advanced Python Programming",
        "instructor": "Henson, M",
        "schedule": "Th 6:00 PM - 7:50 PM",
    },
    "CIS2541": {
        "name": "C++ Language Programming",
        "instructor": "Henson, M",
        "schedule": "T 6:00 PM - 8:50 PM",
    },
}

def menu():
    print(f"1. Find the class in the database")
    print(f"2. Exit")

def normalize_class_code(class_code):
    #deleting-spaces-and-other-useless-stuff
    return class_code.replace("-", "").replace(" ", "").upper() 

def get_class_info(class_code):
    normalized_code = normalize_class_code(class_code)
    
    info = class_info.get(normalized_code)
    
    return info

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter the number from the menu: ")
        match choice:
            case "1":
                class_code = input("Enter a class code: ")
                info = get_class_info(class_code)
    
                if info:
                    print("_____________________________________\n")
                    print(f"Class Code: {class_code}")
                    print(f"Class Name: {info['name']}")
                    print(f"Instructor: {info['instructor']}")
                    print(f"Schedule: {info['schedule']}")
                    print("_____________________________________\n")
                else:
                    print("Class not found in the database.")
            case "2":
                exit()
            case _:
                continue
