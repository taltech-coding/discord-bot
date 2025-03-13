from discord.ext import commands

class Dog(commands.Cog):
    # TODO: 3. ASCII koer
    def __init__(self, bot):
        pass
    # self.bot = ???

    # TODO
    @commands.command(name="mouse", help="Draw a dog")
    async def create_dog(self, ctx):
        pass
    # proovi avada ja lugeda failina open("../dog", "r"). Seejärel saada loetu ctx.send(f"{*eelnev*}") meetodiga

# TODO
def setup(bot):
    pass
# bot.add_cog() vajab selle klassi nime ja klassinimi tahab bot muutujat.