class AssistantBot:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, *args):
        try:
            name, phone_number = args
            self.contacts[name] = phone_number

            return f"Contact {name} added."
        except ValueError:
            return 'Invalid number of arguments'

    def change_contact(self, *args):
        try:
            name, new_phone_number = args

            if name in self.contacts:
                self.contacts[name] = new_phone_number
                return f"Contact {name} updated."
            else:
                return f"Contact {name} not found."
        except ValueError:
            return 'Invalid number of arguments'


    def show_phone(self, *args):
        try:
            name, = args

            if not name:
                raise ValueError

            if name in self.contacts:
                return f"{name}'s phone number: {self.contacts[name]}"
            else:
                return f"Contact {name} not found."
        except ValueError:
            return 'Invalid number of arguments'

    def show_all(self):
        if not self.contacts:
            return "No contacts saved."
        else:
            output = "List of contacts:\n"
            for name, phone_number in self.contacts.items():
                output += f"{name}: {phone_number}\n"

            return output

    def parse_input(self, user_input):
        cmd, *args = user_input.split(' ')
        cmd = cmd.strip().lower()

        return cmd, *args

    def main(self):
        print("Welcome to Assistant Bot!")
        print("Available commands:")
        print("- hello")
        print("- add [name] [phone_number]")
        print("- change [name] [new_phone_number]")
        print("- phone [name]")
        print("- all (to show all contacts)")
        print("- exit (or close to exit)")

        while True:
            user_input = input("Enter a command: ")
            command, *args = self.parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(self.add_contact(*args))
            elif command == "change":
                print(self.change_contact(*args))
            elif command == "phone":
                print(self.show_phone(*args))
            elif command == "all":
                print(self.show_all())
            else:
                print("Invalid command.")


if __name__ == "__main__":
    bot = AssistantBot()
    bot.main()
