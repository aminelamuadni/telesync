"""
Console UI module for the Telesync application.

Author: Amine Lamuadni
Version: 1.0.0
GitHub: https://github.com/aminelamuadni/telesync
"""

import os
from config import settings

class ConsoleUI:
    """
    A class for handling the console-based user interface of the Telesync application.
    """

    def welcome(self):
        """
        Prints a welcome message to the user.
        """

        # Display the welcome message
        print("\nWelcome to Telesync!")

    def agree_to_terms(self):
        """
        Displays the terms and conditions to the user and prompts for their agreement.

        :return: A boolean value indicating whether the user agreed to the terms (True) or not (False).
        """

        # Display the terms and conditions
        terms = """
Please read and agree to the following terms and conditions before using Telesync:

1. By using Telesync, you agree to comply with all applicable laws and regulations related to the use of the Telegram API.

2. You are responsible for any content you access, send or receive using Telesync. You must ensure that any content you send or receive is legal and does not infringe on any intellectual property rights or other legal rights.

3. The developers of Telesync are not liable for any damages or losses resulting from the use of the software. This includes but is not limited to any loss of data, loss of profits, or damage to your device or software.

4. The software is provided "as is" without any warranty, express or implied. The developers of Telesync do not guarantee that the software will be error-free, virus-free, or will meet your specific requirements.

5. You are solely responsible for your use of the Telegram API through Telesync, including any messages or other content you send or receive using the software.

6. By using Telesync, you agree to allow the developers of the software to collect and use data about your use of the software, including but not limited to your IP address, device information, and usage data.

7. You agree not to use Telesync for any illegal, unethical, or unauthorized purposes, including but not limited to spamming, harassment, or sending unsolicited messages or content."""
        print(terms)

        # Prompt the user for input until a valid choice is made
        while True:
            user_input = input("\nDo you agree to these terms and conditions? (Y/N) or type 'exit' to quit: ").lower().strip()
            if user_input == 'y':
                break
            elif user_input == 'n':
                print("\nYou must agree to the terms and conditions to use Telesync.")
            elif user_input == 'exit':
                self.exit_program()
            else:
                print("\nInvalid input. Please enter 'Y' for yes or 'N' for no.")

        return user_input == 'y'

    def choose_option(self):
        """
        Prompts the user to choose an option from a list of available options.

        :return: A string representing the user's choice.
        """

        # Display the available options
        options = """
Please choose an option:

1. Export participants
2. Send messages"""
        print(options)

        # Prompt the user for input until a valid choice is made
        while True:
            choice = input("\nEnter the number of your choice (1-2) or type 'exit' to quit: ").lower().strip()
            if choice in ['1', '2']:
                break
            elif choice == 'back':
                return None
            elif choice == 'exit':
                self.exit_program()
            else:
                print("\nInvalid input. Please try again.")

        return choice

    def choose_entity_type(self):
        """
        Prompts the user to choose an entity type (group or channel).

        :return: A string representing the user's choice.
        """

        # Display the available entity types
        entity_types = """
Please choose an entity type:

1. Group
2. Channel"""
        print(entity_types)

        # Prompt the user for input until a valid choice is made
        while True:
            choice = input("\nEnter the number of your choice (1-2) or type 'back' to go back or 'exit' to quit: ").lower().strip()
            if choice in ['1', '2']:
                break
            elif choice == 'back':
                return None
            elif choice == 'exit':
                self.exit_program()
            else:
                print("\nInvalid input. Please try again.")

        return choice

    def choose_entity(self, entities, entity_type):
        """
        Prompts the user to choose an entity from a list of available entities.

        :param entities: A list of available entities.
        :param entity_type: A string representing the type of entity (group or channel).
        :return: The chosen entity.
        """

        # Prompt the user for input until a valid choice is made
        while True:
            # Display the available entities
            print(f"\nPlease choose a {entity_type}:\n")

            for i, entity in enumerate(entities, start=1):
                print(f"{i}. {entity.title}")
            choice = input(f"\nEnter the number of your choice (1-{len(entities)}) or type 'back' to go back or 'exit' to quit: ").lower().strip()
            if choice in ['exit', 'back'] or choice.isnumeric() and 1 <= int(choice) <= len(entities):
                break
            else:
                print("\nInvalid input. Please try again.")

        if choice == 'back':
            return None
        elif choice == 'exit':
            self.exit_program()
        else:
            return entities[int(choice) - 1]


    def choose_file(self, files, file_type):
        """
        Prompts the user to choose a file from a list of available files.

        :param files: A list of available files.
        :param file_type: A string representing the type of file.
        :return: The chosen file.
        """

        # Display the available files
        print(f"\nPlease choose a {file_type} file:\n")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        # Prompt the user for input until a valid choice is made
        while True:
            choice = input(f"\nEnter the number of your choice (1-{len(files)}) or type 'back' to go back or 'exit' to quit: ").lower().strip()
            if choice in ['exit', 'back'] or choice.isnumeric() and 1 <= int(choice) <= len(files):
                break
            else:
                print("\nInvalid input. Please try again.")

        if choice == 'back':
            return None
        elif choice == 'exit':
            self.exit_program()
        else:
            return files[int(choice) - 1]

    def get_delay_time(self):
        """
        Prompts the user to enter the delay time between messages.

        :return: An integer representing the delay time in seconds.
        """

        # Prompt the user for input until a valid delay time is provided
        while True:
            delay_time = input(f"\nEnter delay time between messages (in seconds) or type 'back' to go back or 'exit' to quit (default: {settings.DELAY_TIME}): ").lower().strip()
            if delay_time == 'back' or delay_time == 'exit' or delay_time.isnumeric() or delay_time == '':
                break
            else:
                print("\nInvalid input. Please try again.")

        if delay_time == 'back':
            return None
        elif delay_time == 'exit':
            self.exit_program()
        elif delay_time == '':
            return settings.DELAY_TIME
        else:
            return int(delay_time)

    def clear_console(self):
        """
        Clears the console screen.
        """

        # Clear the console based on the operating system
        os.system('cls' if os.name == 'nt' else 'clear')

    def exit_program(self):
        """
        Exits the program with a goodbye message.
        """

        # Display the goodbye message and exit the program
        print("\nGoodbye!")
        exit()
