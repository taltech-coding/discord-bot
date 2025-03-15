from discord.ext import commands

class Dog(commands.Cog):
    """ 
    TODO 4.1: Add refernce to the bot. 
    """ 
    def __init__(self, bot):
        self.bot = bot  # Reference goes here (ie the paramater that is inside the brackets above)


    @commands.command(name="dog", help="Draw a dog")  # Change the command name (if you want to)
    async def create_dog(self, ctx):
        """
        TODO 4.2 Fix the name of the command, read data from the file and send a message to discord.
        """
        try:
            with open("dog", "r") as file:  # Change the filename to the name given
                content = file.read()   # Add a read function
                await ctx.send(f"```{content}```")  # In the curly brackets add the content of the file
        except Exception as e:
            print("Error while executing the dog command (see TODO 4.2)\n", e)

async def setup(bot):
    await bot.add_cog(Dog(bot))
