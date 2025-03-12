import pathlib

from dotenv import dotenv_values
from discord import Intents, Message
from discord.ext import commands

from response import get_response

config = dotenv_values(".env")
intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)

# TODO 1: Print a message that the bot is up and running bot's name is stored in client.name
@client.event
async def on_ready():
    BOT_NAME = "[GET THE BOT NAME]"
    print(BOT_NAME, "is now running!")

# TODO 2: Read the messages and choose what to do with the content of them
# The received message is stored in message.content
@client.event
async def on_message(message: Message):
    if ... .startswith("?"):
        await client.process_commands(message)
        return

def main():
    token = config.get("TOKEN")
    if token is None:
        raise ValueError("loo fail nimega .env ja pane sinna TOKEN=isiklik Discord Developer Portal token")
    client.run(token)


if __name__ == "__main__":
    main()