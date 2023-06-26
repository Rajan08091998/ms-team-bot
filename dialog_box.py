from botbuilder.core import CardFactory


def create_dialog_card():
    

    card_data =  {
        "type": "AdaptiveCard",
        "body": [
            {
                "type": "Input.Text",
                "id": "city",
                "placeholder": "Enter City Name"
            },
            
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Submit",
            }
        ]
    }
    
    
    return CardFactory.adaptive_card(card_data)

