"""
Logger module for the Telesync application.

Author: Amine Lamuadni
Version: 1.0.0
GitHub: https://github.com/aminelamuadni/telesync
"""

import logging
import os
from config.settings import LOGS_FOLDER

class Logger:
    """
    A class for handling logging in the Telesync application.
    """

    def __init__(self, name):
        """
        Initializes the Logger with a given name.

        :param name: A string representing the logger's name.
        """

        self.logger = logging.getLogger(name)

    def info(self, message):
        """
        Logs an info level message.

        :param message: A string representing the message to log.
        """

        self.logger.info(message)

    def warning(self, message):
        """
        Logs a warning level message.

        :param message: A string representing the message to log.
        """

        self.logger.warning(message)

    def error(self, message):
        """
        Logs an error level message.

        :param message: A string representing the message to log.
        """

        self.logger.error(message)

def setup_logging():
    """
    Sets up the logging configuration for the Telesync application.
    """

    # Set the logging format string
    log_format = "%(asctime)s [%(levelname)s] %(message)s"

    # Create the logs folder if it doesn't exist
    if not os.path.exists(LOGS_FOLDER):
        os.makedirs(LOGS_FOLDER)

    # Create a file handler for the activity log
    activity_file_handler = logging.FileHandler(os.path.join(LOGS_FOLDER, "activity_log.txt"))
    activity_file_handler.setLevel(logging.INFO)
    activity_file_handler.setFormatter(logging.Formatter(log_format))

    # Create a file handler for the error log
    error_file_handler = logging.FileHandler(os.path.join(LOGS_FOLDER, "error_log.txt"))
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(logging.Formatter(log_format))

    # Create a console handler for displaying log messages in the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(log_format))

    # Configure the root logger with the file and console handlers
    logging.basicConfig(
        level=logging.INFO,
        handlers=[activity_file_handler, error_file_handler, console_handler]
    )
