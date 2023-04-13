"""
Signal Handler module for the Telesync application.

Author: Amine Lamuadni
Version: 1.0.0
GitHub: https://github.com/aminelamuadni/telesync
"""

from signal import signal, SIGINT
from sys import exit
from telesync.ui.console_ui import ConsoleUI
from telesync.utils.logger import Logger

class SignalHandler:
    """
    A class for handling signals in the Telesync application, such as SIGINT or CTRL-C.
    """

    def __init__(self):
        """
        Initializes the SignalHandler with a logger and a console user interface.
        """

        self.logger = Logger(__name__)
        self.console_ui = ConsoleUI()

    def handle_sigint(self, signal_received, frame):
        """
        Handles the SIGINT signal or CTRL-C event by logging a warning message and exiting the program gracefully.

        :param signal_received: The signal received by the handler.
        :param frame: The current stack frame.
        """

        # Print an empty line for better formatting
        print("")
        # Log a warning message
        self.logger.warning("SIGINT or CTRL-C detected. Exiting gracefully")
        # Exit the program gracefully using the console user interface
        self.console_ui.exit_program()

    def setup_signal_handler(self):
        """
        Sets up the signal handler for SIGINT or CTRL-C events.
        """

        # Set the signal handler for SIGINT or CTRL-C events
        signal(SIGINT, self.handle_sigint)
        # Print an empty line for better formatting
        print("")
        # Log an informational message
        self.logger.info("Signal handler has been set up for SIGINT or CTRL-C")
