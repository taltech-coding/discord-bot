from discord.ext import commands
from quotes import get_quote


class Quotes(commands.Cog):
    def __init__(self, bot):
        """TODO 5.2: Get a refernce of the bot"""
        self.bot = bot
    
    
    @commands.command(name="quote", help="get a random quote")
    async def quote(self, ctx):
        """TODO 5.3: Send back a random quote, use the previously made function get_quote(). Sending a response is also viewable in dog.py"""
        await ctx.send(get_quote())

"""TODO 5.3: setup the command (look at the Dog.py file's setup() method on how to do it). Also don't forget to replace here the Dog with Quotes """
async def setup(bot):
    await bot.add_cog(Quotes(bot))
