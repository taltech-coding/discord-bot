from discord.ext import commands

class Dog(commands.Cog):
    """ 
    TODO 4.1: Add refernce to the bot. 
    """ 
    def __init__(self, bot):
        self.bot = ...  # Reference goes here (ie the paramater that is inside the brackets above)


    @commands.command(name="mouse", help="Draw a dog")  # Change the command name
    async def create_dog(self, ctx):
        """
        TODO 4.2 Fix the name of the command, read data from the file and send a message to discord.
        """
        # try:
        #     with open("filename", "r") as file:  # Change the filename to the name given
        #         content = ...  # Read the contents of the file
        #         await ctx.send(f"```{}```")  # In the curly brackets add the content of the file
        # except Exception as e:
        #     print("Error while executing the dog command (see TODO 4.2)\n", e)

async def setup(bot):
    await bot.add_cog(Dog(bot))
