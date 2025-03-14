# 🚀 ChatBoti Töötuba

- [Sissejuhatus](#sissejuhatus)
- [Setup](#Setup)
    - [🤖 Boti käivitamine](#-Boti-käivitamine)
    - [💬 Sõnumite lugemine](#-Sõnumite-lugemine)
    - [🎲 Märgusõnadele vastamine](#-Märgusõnadele-vastamine)
    - [📜 Tsiteerimine](#-Tsiteerimine)
    - [🐶 ASCII koer](#-ASCII-koer)
    - [🔄Extra](#-Extra)


## Sissejuhatus
Sinu väike käsilane sõprade spämmimises, vaenlaste luuramises ja raha teenimises!

Täna loome Discordis töötava Chatbox-stiilis boti.
Ülesannete näidislahendused leiad solutions kaustast!

## Setup
Kõigepealt suundu terminali ja sisesta:
````
pip install discord.py python-dotenv
````
Nüüd loo `.env` fail ja määra sinna oma Discordi boti token:
````
TOKEN=siia_oma_boti_token
````

## 🤖 1. Boti käivitamine
Failis __main.py__ on __on_ready()__ meetod,mis käivitub esimesena kui bot käivitub. 
Lisa sinna __print__ lause, mis annaks märku, et bot käivitus. Selleks kasuta __client.user__ muutujat.
Pea meeles, et iga __async__ meetod tahab __await__ sõna ette, kui tegutsetakse boti või failist lugemisega, kui mitte __print__ lause! 

Kui kõik on õigesti seadistatud, saad boti käivitada:
````
python main.py
````
Kui bot ühendub edukalt, peaksid terminalis nägema kõigepealt 2 punast rida ning seejärel oma boti nime.

## 💬 2. Märgusõnadele vastamine
Liigu faili __response.py__

1. Lisa sõnastikku __responses__ võtmeks mõni märgusõna ja väärtuseks lause, mida sa tahad, et bot vastaks chatis märgusõnale.
2. __get_response__ meetodisse lisa __if__ tingimus, kui __user_input__ leidub __responses__ võtmete hulgas, siis tagasta selle võtme väärtus.

Seejärel suundume __main.py__ faili tagasi.

3. __on_message__ meetod loeb igat sõnumit, mida kanalisse kirjutakse ja kõiki andmeid selle sõnumi kohta. 
Näiteks __message.content__ annab sõnumi sisu, __message.author__ sõnumi autor, __message.channel__ sõnumi saatmise kanali jne.
Kasuta __message.content__ meetodit uurimaks, ega pole kirjutatud chatis __response__ sõnastiku mõnda võtit. Kasuta __if__ tingimust, saates sellisel juhul vastuse: `await message.channel.send(?)`.

Testi discordis oma võtmeid sisestades!

## 🐶 4. ASCII koer
Järgmisena hakkame käske tegema. Kõikidele käskudele teeme eraldi klassi __cogs__ kaustas, alustades __dogs.py__ failist.

1. Lisa uus käsk meetodi __create_dog__, mis loeb ASCII-kunsti __dog__ failist.
2. Kõigepealt on vaja kontrollida, kas fail __dog__ eksisteerib ja lisa logimine juhuks, kui fail jääb leidmata. __ctx.send__ sisse pane loetud faili andmed.
__ctx__ parameeter on sarnane __message__ parameetriga __main.py__ failis, temalt saab teada nii sõnumi autori, sisu, kanali ja lisaks saab temaga sõnumit saata __ctx.send__ teel.
````
        try:
            with open("*failinimi siia*", "r") as file:
                content = file.read()
            await ctx.send(f"```{content}```")
        except Exception as e:
            print(f"Error loading dog art: {e}")
````
3. __setup__ meetodis anna botile kaasa __add_cog__ meetod ning selle sisse omakorda klassinimi ja käsk. Sedamoodi saad botile käske lisada.

Nüüd peame taaskord __main.py__ faili  

1. Lisame __on_message__ meetodisse __if__ tingimuse, juhuks kui chatis sõnum algab küsimärgiga. Käskude leidmiseks sõnumite seas on vaja eraldi __client.process_commands(?)__ meetodit.
2. Järgmisena lisa __on_ready__ meetodisse cogs kausta klasside laadimine (kui pole veel kordagi allalaetud). Niimoodi saab bot kohe käivitudes käskudest aru. 
````python
for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            extension = f'cogs.{filename[:-3]}'
            if extension not in client.extensions:
                try:
                    client.load_extension(extension)
                    print(f"Loaded extension: {extension}")
                except Exception as e:
                    print(f"Failed to load extension {extension}: {e}")
````
Testi discordis __?mouse__ pannes!

## 📜 5. Tsiteerimine

1. Teine käsu teeme __cogs__ kaustas __quoting.py__ faili. Seal on vaja defineerida, et __quotes.py__ failist __get_quote__ meetodist saad tsitaadid.
2. Samamoodi lisa __ctx.send__ lause ning lisa botile __setup__ meetodis klass ja meetod.
3. Edasi minegi __quotes.py__ faili __main.py__ faili all ja kirjuta __quotes__ järjendisse mitmerealiselt oma lemmiktsitaate. Kui kirjutad ühte ritta kõik, saad tekstibloki käsku ?quote chatis kirjutades.

Testi discordis __?quote__ pannes!

## 🔄 Extra
Kui oled kõik eelnevad ülesanded lahendanud, proovi teha järgmist:
- Tase ⭐ Kui kasutaja sisestab roll_dice, tagasta suvaline arv. Seda saad __response.py__ __get_response__ meetodisse lisada.
<details>
  <summary>Spoiler</summary>

    def get_response(user_input: str) -> str:
        lowered: str = user_input.lower()
        if "roll dice" in lowered:
            return f":game_die: You rolled: {randint(1, 6)}"
        elif lowered in responses.keys():
            return responses[lowered]
</details>

- Tase ⭐⭐ Lisa uus käsk __!delete__ __[@username]__, mida väljakutsudes bot teavitab:"__[@username]__ has been permanently deleted. Goodbye forever. 👋"
<details>
  <summary>Spoiler</summary>
Leitav on_message meetodis message.author kasutades.
</details>

- Tase ⭐⭐⭐ Lisa meetod, mis salvestab tekstifaili kõik, mida kasutajad sisestavad.