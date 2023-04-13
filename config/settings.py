"""
This module contains settings for the Telesync application.

Author: Amine Lamuadni
Version: 1.0.0
GitHub: https://github.com/aminelamuadni/telesync
"""

# Telegram API credentials
API_ID = 'YOUR_API_ID'  # Replace with your own Telegram API ID
API_HASH = 'YOUR_API_HASH'  # Replace with your own Telegram API hash
PHONE_NUMBER = 'YOUR_PHONE_NUMBER'  # Replace with your own phone number, including country code

# Folder paths
PARTICIPANTS_FOLDER = 'data/participants'  # Path to folder containing participant CSV files
MESSAGES_FOLDER = 'data/messages'  # Path to folder containing message templates
MEDIA_FOLDER = 'media'  # Path to folder containing media files
LOGS_FOLDER = 'logs'  # Path to folder to write log files to

# Time delay between sending messages, in seconds
DELAY_TIME = 10  # Replace with your preferred delay time, in seconds