from discord import Intents
from discord.ext import commands
from dotenv import dotenv_values

config = dotenv_values(".env")
intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} is now running!")


if __name__ == "__main__":
    token = config.get("TOKEN")
    if token is None:
        raise ValueError("loo fail nimega .env ja pane sinna TOKEN=isiklik Discord Developer Portal token")
    client.run(token)