
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Description:
#   A small application with configurable buttons to automate anything.
#   A configurable list of commands to run is associated to each button.
#   The number of buttons , the list of commands is configurable in
#   the .json file
#

# How to run:
#############
# To run with the default .json configuration
#   python .\button_table_app.py
#
# To run with .json configuration
#   python .\button_table_app.py -j my_configuration.json
#
# How to configure:
##################
# Edit button_table_app_config.json)
#    "buttonTable": [
#        {
#            "buttonName": "Indian Red 01", <=== HERE: Change the button name to your liking
#            "buttonCommand": [
#                {
#                    "cmd01": "print(\"Indian Red 01\")" <=== HERE: change to your commands
#                },
#                {
#                    "cmd02": "print(\"indian red\")"
#                }
#            ],
#            "buttonColour": "indian red"
#        },
#
# Additionally for more complex automation, function  can be added to the configuration
# script. For instance: print_path
#        {
#            "buttonName": "Print PATH variable",
#            "buttonCommand": [
#                {
#                    "cmd01": "print_path()" <=== HERE: user more complex automation
#                },
#                {
#                    "cmd02": "print(\"Green 03\")"
#                },
#                {
#                    "cmd03": "print(\"green\")"
#                }
#            ],
#            "buttonColour": "green"
#        },
#
# def print_path():
# """User defined function for more complicated automation"""
############################################################################
# MIT License
#
# Copyright (c) 2025 pc-scylla
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import tkinter as tk
from tkinter import ttk
import argparse
import json
import sys

# Define exit codes
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

# Add some more complicated command here
# ###############################################################
def print_path():
    """
    User defined function for more complicated automation.
    As an example, printing all the path(s) in the PATH
    environment variable.
    """
    import os

    # Get the PATH environment variable
    path_variable = os.environ.get("PATH")

    # Split the paths based on the separator
    paths = path_variable.split(os.pathsep)

    # Print each path
    for path in paths:
        print(path)

def print_error(msg):
    print(f"ERROR: {msg}\n")

class ButtonTableApp:
    """
    run_commands Method:
        A new method run_commands in the ButtonApp class iterates
        through the buttonCommand list and executes all commands
        for the button using exec().

    Button Command Execution:
        The command parameter of each button invokes the
        run_commands method, passing all commands for the button
        as an argument.

    Multiple Commands per Button:
        When a button is clicked, it will sequentially execute
        all commands defined in the JSON file for that button.

    Behavior:
        Each button will execute all commands
        (printing the button name and its color) when clicked.
        The buttons remain organized in two columns for readability
    """
    def __init__(self, app_data):
        """Initialize the Tkinter GUI with the provided app data."""
        self.app_data = app_data
        self.root = tk.Tk()
        self.root.title(app_data['appTitle'])
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        self.create_buttons(self.frame)

        # How to make two columns of buttons to have the same column size
        # i.e. the size of  the bigest text.
        #
        # Ref: stack overflow available at
        # https://stackoverflow.com/questions/21009232/how-to-make-tkinter-columns-of-equal-width-when-widgets-span-multiple-columns
        # accessed 28/03/2025
        #
        self.frame.grid_columnconfigure(0, weight=1, uniform='a')
        self.frame.grid_columnconfigure(1, weight=1, uniform='a')

        # winfo_children stands for "widget info children", and gets all the children of a widget.
        for child in self.frame.winfo_children():
            child.grid_configure(padx=7, pady=7)

    def create_buttons(self, frame):
        """Create buttons from app data and arrange them in a two-column grid."""
        for index, button in enumerate(self.app_data['buttonTable']):
            button_name = button['buttonName']
            button_colour = button['buttonColour'].lower()  # Convert to lowercase for Tkinter compatibility

            # Create a button and place it in grid (2 columns)
            tk.Button(
                frame,
                text=button_name,
                bg=button_colour,
                command=lambda cmds=button['buttonCommand']: self.run_commands(cmds)  # Execute all commands
            ).grid(row=index // 2, column=index % 2, padx=5, pady=5, sticky="EW")

    def run_commands(self, commands):
        """Execute all commands associated with a button."""
        for command in commands:
            for key, value in command.items():
                # Print the key and the command
                print(f"Executing {key}: {value}")
                exec(value)

    def run(self):
        """Run the main Tkinter event loop."""
        self.root.mainloop()

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
    description=r"Configurable Button Table Application e.g. python .\button_table_app.py -j .\button_table_app_config.json.")

    parser.add_argument(
        "-j", "-json",
        type=str,
        default=r".\button_table_app_config.json",
        help="Path to the JSON file (default: button_table_app_config.json)"
    )

    args = parser.parse_args()

    # Read the JSON file
    try:
        with open(args.j, "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print(f"Error: File '{args.j}' not found.")
        sys.exit(EXIT_FAILURE)
    except json.JSONDecodeError:
        print(f"Error: File '{args.j}' is not a valid JSON file.")
        sys.exit(EXIT_FAILURE)

    app = ButtonTableApp(data)
    app.run()

    # If everything runs successfully
    sys.exit(EXIT_SUCCESS)

if __name__ == "__main__":
    main()