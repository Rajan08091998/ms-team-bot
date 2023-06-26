from weather import weather
from dialog_box import BlackDialog


def command1_handler():
    # Logic for handling command 1
    dialog = BlackDialog(None, "Enter Your City")

    # Access the user's input
    city = dialog.result
    text = weather(city)
    
    return text


def get_command_handler(command_name):
    if str(command_name).lower() == "/weather":
        return command1_handler
    else:
        return None