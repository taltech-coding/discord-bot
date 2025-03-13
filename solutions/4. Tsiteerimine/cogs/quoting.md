## Quotes
Impordime quotes klassi __get_quote__ meetodi ja võime defineerida ka kirjelduse ja nime, mida ?help käsku kirjutades chati kuvatakse.
```py
from discord.ext import commands
from quotes import get_quote

class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="quote", help="get a random quote")
    async def quote(self, ctx):
        await ctx.send(get_quote())

def setup(bot):
    bot.add_cog(Quotes(bot))
```