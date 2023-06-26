from dialog_box import create_dialog_card


def city_card_command_handler():    
    return create_dialog_card()


def get_command_handler(command_name):
    if str(command_name).lower() == "/weather":
        return city_card_command_handler
    else:
        return None