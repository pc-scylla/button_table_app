# Button Table Application

## Description
A small application with configurable buttons designed to automate various tasks. Each button is linked to a customizable list of commands that can be executed. The number of buttons and associated commands are fully configurable via a `.json` configuration file.

## Features
- Configurable buttons to automate tasks.
- Customizable commands for each button.
- Flexible `.json` configuration file for managing buttons, commands, and more.

## How to Run

### Run with Default Configuration
```bash
python .\button_table_app.py
```

### Run with Custom `.json` Configuration
```bash
python .\button_table_app.py -j my_configuration.json
```

## How to Configure

1. Open the `button_table_app_config.json` file.
2. Modify the `buttonTable` section to add or edit buttons and their commands.

### Example Configuration
```json
"buttonTable": [
    {
        "buttonName": "Indian Red 01",
        "buttonCommand": [
            {
                "cmd01": "print(\"Indian Red 01\")"
            },
            {
                "cmd02": "print(\"indian red\")"
            }
        ],
        "buttonColour": "indian red"
    },
    {
        "buttonName": "Print PATH variable",
        "buttonCommand": [
            {
                "cmd01": "print_path()"
            },
            {
                "cmd02": "print(\"Green 03\")"
            },
            {
                "cmd03": "print(\"green\")"
            }
        ],
        "buttonColour": "green"
    }
]
```

### Advanced Automation
For more complex tasks, user-defined functions can be integrated into the configuration script. Example:
```python
def print_path():
    """User-defined function for more complicated automation""" 
    print("PATH variable:") 
    print(os.environ["PATH"])
```

Add this function to the `buttonCommand` section as:
```json
{ 
    "cmd01": "print_path()" 
}
```

## Requirements
- Python 3.x
- Dependencies listed in `requirements.txt`


---

Feel free to let me know if you'd like further assistance!
