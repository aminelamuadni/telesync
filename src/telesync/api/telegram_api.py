"""
Telegram API module for interacting with the Telegram platform.

Author: Amine Lamuadni
Version: 1.0.0
GitHub: https://github.com/aminelamuadni/telesync
"""

import asyncio
import pandas as pd
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors import ChatAdminRequiredError
from config.settings import API_ID, API_HASH, PHONE_NUMBER

class TelegramApi:
    """
    A class for interacting with the Telegram platform using Telethon.
    """

    def __init__(self):
        # Initialize the TelegramClient with API_ID, API_HASH, and PHONE_NUMBER
        self.client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)

    async def start(self):
        """
        Starts the Telegram client.
        """

        await self.client.start()

    async def get_entities(self, entity_type):
        """
        Retrieves a list of entities (groups or channels) from the user's Telegram dialogs.

        :param entity_type: A string representing the type of entity ("group" or "channel").
        :return: A list of matching entities.
        """

        dialogs = await self.client.get_dialogs()
        entities = []
        if entity_type == "channel":
            entities = [dialog for dialog in dialogs if dialog.is_channel and not dialog.is_group]
        elif entity_type == "group":
            entities = [dialog for dialog in dialogs if dialog.is_group]
        return entities

    async def get_participants(self, chosen_entity):
        """
        Retrieves a list of participants in the specified entity (group or channel).

        :param chosen_entity: The entity from which to retrieve participants.
        :return: A list of participants.
        """

        participants = []
        try:
            async for user in self.client.iter_participants(chosen_entity):
                participants.append(user)
        except ChatAdminRequiredError:
            print("Error: You do not have admin privileges in this group.")
        return participants

    async def send_messages(self, participants, messages, delay_time):
        """
        Sends messages to the specified participants with a delay between each message.

        :param participants: A list of participants to send messages to.
        :param messages: A list of messages to send.
        :param delay_time: The time in seconds to wait between sending messages.
        """

        async def send_message_async(participant, message):
            try:
                # Get the input entity (user) based on their username or phone number
                if 'username' in participant and not pd.isna(participant['username']):
                    receiver = await self.client.get_input_entity(participant['username'])
                elif 'phone_number' in participant and not pd.isna(participant['phone_number']):
                    entity = await self.client.get_input_entity(participant['phone_number'])
                    receiver = InputPeerUser(entity.user_id, entity.access_hash)
                else:
                    print(f"No username or phone number found for participant {participant}")
                    return

                # Send the message with or without media files
                if 'message_media' in message and message['message_media']:
                    media_list = []
                    for media in message['message_media']:
                        media_list.append(await self.client.upload_file(media))

                    await self.client.send_message(receiver, file=media_list, message=message['message_text'])
                else:
                    await self.client.send_message(receiver, message['message_text'])

                # Print a success message
                if not pd.isna(participant['username']):
                    print(f"Sent message to username {participant['username']}")
                elif not pd.isna(participant['phone_number']):
                    print(f"Sent message to phone number {participant['phone_number']}")
            except Exception as e:
                # Print an error message if there was a problem sending the message
                if not pd.isna(participant['username']):
                    print(f"Error sending message to {participant['username']}: {str(e)}")
                elif not pd.isna(participant['phone_number']):
                    print(f"Error sending message to {participant['phone_number']}: {str(e)}")

        for message in messages:
            for participant in participants:
                await send_message_async(participant, message)
                print(f"Waiting for {delay_time} seconds before sending the next message")
                await asyncio.sleep(delay_time)
