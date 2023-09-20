
companyName = input("Enter company's name: ")

myCompany = {}
_name = ""

while True:
    _name = input("Enter next employee's name ('q' to quit): ")
    if _name != 'q':
        myCompany[_name] = input("Enter employee's job: ")
    else:
       break

print(f"\n{companyName}")
print(f"------------------------------------------------------------")
for name in myCompany:
    print(f"\t{name}\t: {myCompany[name]}")
print(f"------------------------------------------------------------")
