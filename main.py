import pathlib

from dotenv import dotenv_values
from discord import Intents, Message
from discord.ext import commands

from response import get_response

config = dotenv_values(".env")
intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)

# TODO: 1. Boti käivitamine ja 4. Tsiteerimine
@client.event
async def on_ready():
    pass
# client.user kuvab boti nime

# pathlib.Path("cogs").rglob("*.py") leiab cogs kausta ja  client.load_extension(".".join(file.with_suffix("").parts)) teeb "laisa laadimise"

# TODO: 2. Sõnumite lugemine ja 3. ASCII koer
@client.event
async def on_message(message: Message):
    pass
# võtme saad get_response(message.content) kasutades ning chati saad väärtust saata await.message.channel.send(*eelnev*) pannes

# message.content.startswith("?") abil tuvastad käsud ning seejärel kasuta client.process_commands(message )meetodit


if __name__ == "__main__":
    token = config.get("TOKEN")
    if token is None:
        raise ValueError("loo fail nimega .env ja pane sinna TOKEN=isiklik Discord Developer Portal token")
    client.run(token)
