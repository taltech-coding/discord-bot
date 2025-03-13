from discord.ext import commands
from quotes import get_quote


class Quotes(commands.Cog):
    # TODO: 4. Tsiteerimine
    def __init__(self, bot):
        pass
    # self.bot = ???
    
    # TODO
    @commands.command(name="quote", help="get a random quote")
    async def quote(self, ctx):
        pass
    # ctx.send() sisse saab panna meetodi, mida siis käsuna rakendatakse.

# TODO
def setup(bot):
    pass
# bot.add_cog() vajab selle klassi nime ja klassinimi tahab bot muutujat.