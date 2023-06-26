# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext,MessageFactory
from botbuilder.schema import ChannelAccount
from command_handler import get_command_handler,city_card_command_handler
from weather import weather


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        # await turn_context.send_activity(f"{ turn_context.activity.text }")
        command_name = turn_context.activity.text

        command_handler = get_command_handler(command_name)
        if command_handler:
            card = city_card_command_handler()
            await turn_context.send_activity(MessageFactory.attachment(card))

        elif turn_context.activity.value:
            city = turn_context.activity.value['city']
            text = weather(city)
            
            await turn_context.send_activity(f'{text}')

        else:
            await turn_context.send_activity(f"You Typed: { turn_context.activity.text }")


    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
