from discord.ext import commands
from quotes import get_quote


class Quotes(commands.Cog):
    # TODO
    def __init__(self, bot):
        pass

    # TODO
    @commands.command(name="quote", help="get a random quote")
    async def quote(self, ctx):
        pass

# TODO
async def setup(bot):
    pass
