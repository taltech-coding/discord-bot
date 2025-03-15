## Dog.py ehk ASCII kunst käsuga

### Dog isend
```py
from discord.ext import commands
```

Kuna Dog klass kasutab funktsionaalsust, mis nõuab main.py failis olevaid andmeid (klient, token, erinevad importid), 
siis võtame Cog klassi abiga, pärides __commands.Cog__ laiendit. 
```py
class Dog(commands.Cog):
```

__init__ on meetod, millega lisame Boti Dog klassile.
```py
    def __init__(self, bot):
        self.bot = bot 
```

__@commands.command__ on sama eesmärgiga dekoraator nagu __@client.command()__, asukoht projektis vaid erinev.
Me võime (kuid ei pea) ?help käsule kaasa anda kirjelduse ja nime meie uuest käsust. 
Muidu kuvatakse klassinimi kirjelduseta.
```py
    @commands.command(name="mouse", help="Draw a dog")
```

__ctx__ on kontekst ehk info nagu kes kirjutas, mis kanalis, kas privaatkanalis jne.
```py
    async def create_dog(self, ctx):
```

__try__ on juhuks, kui arvuti ei leia "dog" faili, et ilmuks terminali veateade. Ilma selleta jookseks Bot kokku, kui ei leia faili.
"r" sümboliseerb "read"-režiimi et avame faili "dog" ja loeme faili sisu "content" muutujasse.
```py
        try:
            with open("dog", "r") as file:          
                content = file.read()
```

__ctx.send__ tagab selle, et saadame õigesse kanalisse __content__ sõnumi ehk koera ASCII.
``` py
            await ctx.send(f"```{content}```")
        except Exception as e:
            print(f"Error loading dog art: {e}")
```


### main.py ja Dog isendi sidumine

main.py klassis cog kausta alla laadides otsitakse kõigepealt __setup__ meetodit ja __setup__ meetodi abil saame koera isendi alles luua.
__add_cog__ meetod laseb meil automaatselt registeerida selle klassi käsud.
```py
async def setup(bot):
    await bot.add_cog(Dog(bot))

```