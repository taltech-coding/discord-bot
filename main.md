## Main.py

### Importime load, tokeni ja määrame käsu algus-karakteri

__Intents__ on "load", mille andsime Discord Developer Portalis Botile.
__commands__ abil saab Bot reageerida käskudele.
```
from discord import Intents
from discord.ext import commands
```
Laeme enda .env-failide leidmiseks vajaliku liidese.
```
from dotenv import dotenv_values
```
Salvestame __config__ muutujasse tokeni väärtuse, otsides tervest projektist .env nimelisi faile ja kaustu.
```
config = dotenv_values(".env")
```
__Intents.default()__ on Boti lubamise standard ehk mida on Botil õigus teada ja millistele sündmustele 
(näiteks sõnumi saatmine) tohib Bot vastata. Neid õiguseid peab andma nii Discord Developer Portali lehel kui enda koodis
turvalisuse pärast.
```
intents = Intents.default()

```
__intents.message_content__ annab Botile õiguse kirjutada chatis. Samamoodi võib muuta ka Boti staatuse "invisible" ```intents.typing = False```
või võtta ära "typing" animatsiooni ``` intents.presences = False``` reaga.
```
intents.message_content = True
```
Kuulutame küsimärgiga algavad sõnad Boti käskudeks ning anname botile standard õigused pluss chati kirjutamise õigus.
```
client = commands.Bot(command_prefix="?", intents=intents)
```

### Botile funktsionaalsust
__async__ on JavaScripti meetod, mis laseb asünkroonsel meetodil tunduda sünkroonnena. 
__async__ abil lubame arvutile, et me anname talle vastuse, kuid pole vaja oodata meie järgi.

__@client.event__ on dekoraator. Dekoraator on meetod, milles juba leidub funktsionaalsust, kuid mis lubab meil lisada omi laiendusi/piiranguid.
__@client.event__  dekaraatoril juba eksisteerivad meetodid nagu __on_ready()__, __on_message()__ ja __on_member_join()__.
__on_ready()__ meetod käivitub iga kord kui Bot aktiviseerub ehk jooksma pannakse.
```
@client.event
async def on_ready():
    print(f"{client.user} is now running!")
```

### Boti tööle panemine

Käivitame Boti tokeni väärtusega ja ühendame Discordi serveriga.
```
if __name__ == "__main__":
   token = config.get("TOKEN")
       if token is None:
           raise ValueError("loo fail nimega .env ja pane sinna BOT_TOKEN=isiklik Discord Developer Portal token")
       client.run(token)
```
