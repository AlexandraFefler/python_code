contacts = {}
command = input("Enter command (add, remove, exit): ")
while command.lower() != "exit":
    if command.lower() == "add":
        name = input("Enter name: ")
        while name in contacts:
            name = input(f"contact with this name already exists.\nEnter name: ")
        tel = input("Enter tel. number: ")
        while not(tel.isnumeric()):
            tel = input("Invalid tel. number.\nEnter tel. number: ")
        contacts[name] = tel
    elif command.lower() == "remove":
        remove_name = input("Enter name of contact to remove: ")
        while not(name in contacts):
            remove_name = input(f"contact with this name doesn't exist.\nEnter name of contact to remove: ")
        del contacts[remove_name]
    command = input("Enter command (add, remove, exit): ")
print(contacts)
