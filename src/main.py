"""
Main module for the Telesync application.

Author: Amine Lamuadni
Version: 1.0.0
GitHub: https://github.com/aminelamuadni/telesync
"""

import asyncio
from telethon.tl.custom.dialog import Dialog
from telesync.api.telegram_api import TelegramApi
from telesync.handlers.csv_handler import CSVHandler
from telesync.ui.console_ui import ConsoleUI
from telesync.utils.logger import Logger, setup_logging
from telesync.utils.signal_handler import SignalHandler

async def main():
    """
    Main function to run the Telesync application.
    This function initializes the necessary classes, sets up the logging and signal handling,
    displays the welcome message, and provides the main application loop.
    """

    # Initialize necessary classes
    logger = Logger(__name__)
    signal_handler = SignalHandler()
    console_ui = ConsoleUI()
    api = TelegramApi()
    csv_handler = CSVHandler()

    # Set up logging and signal handling
    setup_logging()
    signal_handler.setup_signal_handler()

    # Display the welcome message and check if the user agrees to the terms
    console_ui.welcome()
    if not console_ui.agree_to_terms():
        return

    # Start the Telegram API client
    await api.start()

    # Main application loop
    while True:
        # Get the user option from the console UI
        user_option = console_ui.choose_option()

        # Option 1: Export participants from a group or channel
        if user_option == "1":
            while True:
                # Get the user's chosen entity type (group or channel)
                user_entity_type = console_ui.choose_entity_type()
                if user_entity_type is None:
                    break

                entity_type = "group" if user_entity_type == "1" else "channel"
                entities = await api.get_entities(entity_type)
                while True:
                    # Get the user's chosen entity (group or channel)
                    user_entity = console_ui.choose_entity(entities, entity_type)
                    if user_entity is None:
                        break
                    elif isinstance(user_entity, Dialog):
                        participants = await api.get_participants(user_entity)
                        if len(participants) > 0:
                            # Save the participants to a CSV file
                            csv_handler.save_participants(participants, user_entity.title)
                        break

        # Option 2: Send messages to participants from a CSV file
        elif user_option == "2":
            while True:
                # Get the user's chosen participants file
                participants_file = console_ui.choose_file(csv_handler.get_participants_files(), "participants")
                if participants_file is None:
                    break

                while True:
                    # Get the user's chosen messages file
                    messages_file = console_ui.choose_file(csv_handler.get_messages_files(), "messages")
                    if messages_file is None:
                        break

                    # Load participants and messages from the CSV files
                    participants = csv_handler.load_participants(participants_file)
                    messages = csv_handler.load_messages(messages_file)

                    while True:
                        # Get the user's chosen delay time between messages
                        delay_time = console_ui.get_delay_time()
                        if delay_time is None:
                            break

                        # Send the messages to the participants with the specified delay time
                        await api.send_messages(participants, messages, delay_time)
                        break

                    break

                break

    # Stop the Telegram API client
    await api.stop()

# Run the main function as an asynchronous coroutine
if __name__ == "__main__":
    asyncio.run(main())
