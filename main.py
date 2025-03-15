import pathlib

from dotenv import dotenv_values
from discord import Intents, Message
from discord.ext import commands

from response import get_response

config = dotenv_values(".env")
intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)

@client.event
async def on_ready():
    """
    TODO 1: Print a message that the bot is up and running, bots name is stored in client.user 
    """
    BOT_NAME = "[GET THE BOT NAME]"
    print(BOT_NAME, "is now running!")
    
    for file in pathlib.Path("cogs").rglob("*.py"):
        try:
            await client.load_extension(".".join(file.with_suffix("").parts))
        except Exception as e:
            print("Couldn't load cogs file (if you haven't gotten to task 4, ignore this error)\n", e)


@client.event
async def on_message(message: Message):
    """ 
    TODO 2: Read the messages and choose what to do with the content of it
    The received message is stored in message.content and we want to check if it starts with the question mark
    If the message doesn't start with a question mark, then answer to that message (this is just for testing)
    """
    # if .startswith("?"):  # TODO: Check if the message.content starts with a question mark
    #     await client.process_commands(message)
    #     return

    """
    TODO 3.1: Get the response and answer to that response.
    """
    # response = get_response()  # TODO: Add in between these brackets the message that the bot received (look at task 2)
    # if response:
    #     await message.channel.send()  # TODO: Add the repsonse that we got from get_response()


def main():
    token = config.get("TOKEN")
    if token is None:
        raise ValueError("loo fail nimega .env ja pane sinna TOKEN=isiklik Discord Developer Portal token")
    client.run(token)


if __name__ == "__main__":
    main()