"""
CSV Handler module for the Telesync application.

Author: Amine Lamuadni
Version: 1.0.0
GitHub: https://github.com/aminelamuadni/telesync
"""

import os
import pandas as pd
from config.settings import PARTICIPANTS_FOLDER, MESSAGES_FOLDER

class CSVHandler:
    """
    A class for handling CSV files related to participants and messages in the Telesync application.
    """

    def __init__(self):
        """
        Initializes the CSVHandler with the proper directories for participants and messages.
        """

        # Set the directory paths for participants and messages
        self.participants_dir = PARTICIPANTS_FOLDER
        self.messages_dir = MESSAGES_FOLDER
        
        # Create directories if they do not exist
        if not os.path.exists(self.participants_dir):
            os.makedirs(self.participants_dir)

        if not os.path.exists(self.messages_dir):
            os.makedirs(self.messages_dir)

    def get_participants_files(self):
        """
        Returns a list of available participant CSV files.

        :return: A list of file names.
        """

        # List all the files in the participants directory
        return os.listdir(self.participants_dir)

    def get_messages_files(self):
        """
        Returns a list of available message CSV files.

        :return: A list of file names.
        """

        # List all the files in the messages directory
        return os.listdir(self.messages_dir)

    def save_participants(self, participants, entity_name):
        """
        Saves the participants to a CSV file.

        :param participants: A list of participant objects.
        :param entity_name: A string representing the entity's name.
        """

        # Create a file name for the CSV file
        file_name = f"{entity_name}_participants.csv".replace(' ', '_')
        file_name = ''.join(e for e in file_name if e.isalnum() or e in ['_', '.'])
        file_path = os.path.join(PARTICIPANTS_FOLDER, file_name)

        # Prepare the data to be saved in the CSV file
        data = {
            "first_name": [],
            "last_name": [],
            "username": [],
            "phone_number": []
        }

        # Collect participant data
        for user in participants:
            if user.phone or user.username:
                data["first_name"].append(user.first_name)
                data["last_name"].append(user.last_name or '')
                data["username"].append(user.username or '')
                data["phone_number"].append(user.phone or '')

        # Check if there are any participants with phone numbers or usernames
        if not data["phone_number"] and not data["username"]:
            print("\nNo participants with phone numbers or usernames found.")
            return

        # Save the participants data to the CSV file
        new_participants_df = pd.DataFrame(data)

        # Update the existing CSV file if it already exists
        if os.path.exists(file_path):
            existing_participants_df = pd.read_csv(file_path)
            combined_df = pd.concat([existing_participants_df, new_participants_df])
            combined_df.drop_duplicates(subset=['username', 'phone_number'], keep='first', inplace=True)
        else:
            combined_df = new_participants_df

        # Write the updated participants data to the CSV file
        combined_df.to_csv(file_path, index=False)
        print(f"\nExported {len(participants)} participants to {file_path}")

    def load_participants(self, file_name):
        """
        Loads participants from a given CSV file.

        :param file_name: A string representing the file name.
        :return: A list of dictionaries containing participant information.
        """

        # Read the participant data from the CSV file
        file_path = os.path.join(self.participants_dir, file_name)
        return pd.read_csv(file_path, dtype=str).to_dict(orient='records')

    def load_messages(self, file_name):
        """
        Loads messages from a given CSV file.

        :param file_name: A string representing the file name.
        :return: A list of dictionaries containing message information.
        """

        # Read the message data from the CSV file
        file_path = os.path.join(self.messages_dir, file_name)
        df = pd.read_csv(file_path)

        # If the CSV file contains a 'message_media' column, process the media data
        if 'message_media' in df.columns:
            df['message_media'] = df['message_media'].apply(lambda x: x.split(';') if not pd.isnull(x) else [])

        # Convert the DataFrame to a list of dictionaries and return the message data
        return df.to_dict(orient='records')
