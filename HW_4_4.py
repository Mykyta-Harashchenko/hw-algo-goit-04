def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Usage: add [name] [phone in +38 format]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Usage: change [name] [phone]"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated successfully."

def show_contact(args, contacts):
    if len(args) != 1:
        return "Invalid arguments. Usage: show [name]"
    name = args[0]
    return contacts.get(name, "Contact not found.")

def all_contact(contacts):
    result = []
    for name, phone in contacts.items():
        result.append({'Name': name, 'Phone': phone})
    return result
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_contact(args, contacts))

        elif command == 'all':
            print(all_contact(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()