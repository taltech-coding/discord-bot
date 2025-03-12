import pathlib

from dotenv import dotenv_values
from discord import Intents, Message
from discord.ext import commands

from response import get_response

config = dotenv_values(".env")
intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)

# TODO
@client.event
async def on_ready():
    pass

# TODO
@client.event
async def on_message(message: Message):
    pass

def main():
    token = config.get("TOKEN")
    if token is None:
        raise ValueError("loo fail nimega .env ja pane sinna TOKEN=isiklik Discord Developer Portal token")
    client.run(token)


if __name__ == "__main__":
    main()