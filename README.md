# Telesync

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Python Installation](#python-installation)
- [Telegram API Setup](#telegram-api-setup)
- [Telesync Installation](#telesync-installation)
- [Usage](#usage)
  - [Export Participants](#export-participants)
  - [Send Messages](#send-messages)
  - [Creating the Message Campaign CSV File](#creating-the-message-campaign-csv-file)
- [Configuration](#configuration)
- [Logs](#logs)
- [Known Issues and Workarounds](#known-issues-and-workarounds)
- [Important Notes](#important-notes)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Version](#version)

## Description

Telesync is a command-line utility that helps users export participant data from Telegram groups and channels, as well as send messages to those participants. The extracted participant data can be saved as CSV files, while messages can be loaded from CSV files and sent to the list of participants. This tool aims to make it easier to manage and communicate with your Telegram group or channel members.

## Features

- Export participants from Telegram groups or channels
- Send messages to exported participants
- Supports text messages and media messages (images, videos, documents)
- Configure delay time between sending messages
- Save participants as CSV files

## Requirements

- Python 3.7 or higher
- Telethon library
- pandas library

## Python Installation

1. Download Python from the official website: https://www.python.org/downloads/
2. Run the installer and follow the installation instructions.
3. Make sure to check the "Add Python to PATH" option during installation.
4. Verify that Python is installed by running `python --version` in your command prompt or terminal.

## Telegram API Setup

1. Go to https://my.telegram.org/auth and log in with your phone number.
2. Click on "API development tools".
3. Fill in the required information and click "Create Application".
4. Note down the `api_id` and `api_hash` values. You will need them to configure the Telegram API in Telesync.

## Telesync Installation

1. Clone the repository or download the source code.
2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

3. Open the `config/settings.py` file and add your Telegram API credentials:

```bash
API_ID = 'YOUR_API_ID'  # Replace with your own Telegram API ID
API_HASH = 'YOUR_API_HASH'  # Replace with your own Telegram API hash
PHONE_NUMBER = 'YOUR_PHONE_NUMBER'  # Replace with your own phone number, including country code
```

Replace `YOUR_API_ID`, `YOUR_API_HASH`, and `YOUR_PHONE_NUMBER` with the values obtained from the Telegram API setup.

## Usage

1. Run the `start.bat` script (Windows) or execute the following command:

```bash
$env:PYTHONPATH = "$env:PYTHONPATH;$(Get-Location)"; python src\main.py
```

2. Follow the on-screen prompts to choose between exporting participants from Telegram groups or channels and sending messages to the exported participants.

### Export Participants

1. Choose the "Export Participants" option.
2. Select the type of entity you want to export participants from (group or channel).
3. Choose the group or channel from the list.
4. The participant data will be saved in a CSV file in the "data/participants" folder.

### Send Messages

1. Choose the "Send Messages" option.
2. Select a CSV file with participant data from the "data/participants" folder.
3. Select a CSV file with message data from the "data/messages" folder.
4. Set the delay time between messages.
5. The messages will be sent to the participants according to the specified delay time.

### Creating the Message Campaign CSV File

To create a CSV file with the campaign messages, follow these steps:

1. Create a new text file and change the file extension to .csv (e.g., campaign_messages.csv).
2. Open the CSV file with a text editor or a spreadsheet software (e.g., Microsoft Excel, Google Sheets, or LibreOffice Calc).
3. Add two columns: message_text and message_media.
4. In the message_text column, write the text content of your messages.
5. In the message_media column, add the file paths of any media you want to send with the message. Separate multiple file paths with a semicolon (;).

Here's an example of a `campaign_messages.csv` file:

```bash
"message_text","message_media"
"Welcome to our community! Enjoy your stay.","C:\Users\<YourUsername>\Images\WelcomeImage.jpg;C:\Users\<YourUsername>\Videos\IntroVideo.mp4"
"Check out our latest updates and news!","C:\Users\<YourUsername>\Documents\Newsletter.pdf"
```

## Configuration

You can configure Telesync by modifying the `config/settings.py` file. The available settings are:

- `API_ID`: Your Telegram API ID. Replace with your own API ID obtained during the Telegram API setup.
- `API_HASH`: Your Telegram API hash. Replace with your own API hash obtained during the Telegram API setup.
- `PHONE_NUMBER`: Your phone number, including the country code. Replace with your own phone number.

- `PARTICIPANTS_FOLDER`: The folder path for storing participant CSV files. Default is `'data/participants'`.
- `MESSAGES_FOLDER`: The folder path for storing message templates. Default is `'data/messages'`.
- `LOGS_FOLDER`: The folder path for storing log files. Default is `'logs'`.

- `DELAY_TIME`: The time delay between sending messages, in seconds. You can replace this with your preferred delay time. Default is `'10'`.

## Logs

- Telesync logs activity and errors to the "logs" folder.
- The `activity_log.txt` file contains general activity information.
- The `error_log.txt` file contains error messages.

## Known Issues and Workarounds

### Arabic and Emojis Showing as Question Marks in Command Prompt

If you experience issues with Arabic text or emojis displaying as question marks in the Command Prompt, try one of the following workarounds:

1. Change the font in Command Prompt:

    - Right-click on the Command Prompt title bar and select "Properties."
    - In the "Font" tab, select a font with better Unicode support, such as "Consolas" or "Lucida Console."
    - Click "OK" to apply the changes.

2. Use a different terminal emulator with better Unicode support, such as Windows Terminal or PowerShell:

    - [Windows Terminal](https://aka.ms/terminal) can be downloaded from the Microsoft Store.
    - PowerShell comes pre-installed on most modern Windows systems. Simply search for "PowerShell" in the Start menu to launch it.

When using an alternative terminal emulator, navigate to the project directory and execute the following command to run Telesync:

```bash
$env:PYTHONPATH = "$env:PYTHONPATH;$(Get-Location)"; python src\main.py
```

## Important Notes

- Telesync is intended for educational purposes and personal use only. Do not use it for spamming or any activity that violates Telegram's terms of service.
- Sending a large number of messages in a short period of time may result in temporary or permanent bans from Telegram.
- The user is solely responsible for any consequences that may arise from using Telesync.

## Contributing

We welcome contributions to Telesync! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with informative commit messages.
4. Push your changes to the branch.
5. Create a pull request, describing the changes you made and why.

Please note that by contributing to this project, you agree to follow the code of conduct and your changes may be subject to review.

## License

Telesync is released under the MIT License. See the `LICENSE` file for more information.

## Author

Amine Lamuadni

## Version

1.0
