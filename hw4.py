def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


