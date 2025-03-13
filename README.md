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

## 🤖 Boti käivitamine
Failis main.py on peamine boti loogika. Kontrolli, kas bot suudab õigesti käivituda ja ühendada serveriga.

Kui kõik on õigesti seadistatud, saad boti käivitada:
````
python main.py
````
Kui bot ühendub edukalt, peaksid terminalis nägema kõigepealt 2 punast rida ning seejärel:

__SinuBotiNimi#1234 is now running!__

## 💬 2. Märgusõnadele vastamine
Liigu faili __response.py__

1. Lisa sõnastikku __responses__ võtmeks mõni märgusõna ja väärtuseks lause, mida sa tahad, et bot vastaks chatis märgusõna peale.
2. __get_response__ meetodisse lisa __if__ tingimus, kui __user_input__ leidub __responses__ võtmete hulgas, siis tagasta selle võtme väärtus.

Seejärel suundume __main.py__ faili tagasi.

1. __on_message__ meetodisse on vaja oma korda küsida ega chati sõnum pole __response__ sõnastikus mõni võti. Kui oli, siis bot saab saata vastuse käsuga: `await message.channel.send(response)`.

Testi discordis oma võtmeid sisestades!

## 🐶 4. ASCII koer
Järgmisema hakkame käske tegema. Kõikidele käskudele teeme eraldi klassi __cogs__ kaustas, alustades __dogs.py__ failist.

1. Kõigepealt kontrolli, kas fail __dog__ eksisteerib ja lisa logimine juhuks, kui fail jääb leidmata.
2. Lisa uus käsk meetodi __create_dog__, mis loeb ASCII-kunsti __dog__ failist.

Nüüd peame taaskord __main.py__ faili  

1. Lisame __on_message__ meetodisse __if__ tingimuse, juhuks kui chatis sõnum algab küsimärgiga. Siis on vaja kasutada käsku __client.process_commands(message)__.
2. Järgmisena lisa __on_ready__ meetodisse "laisk laadimine" cogs kaustale. Niimoodi saab bot kohe käivitudes käskudest aru. 

Testi discordis __?mouse__ pannes!

## 📜 5. Tsiteerimine
Teine käsu teeme __cogs__ kaustas __quoting.py__ faili. Seal on vaja defineerida, et __quotes.py__ failist __get_quote__  
meetodist saad tsitaadid.

Edasi minegi __quotes.py__ faili __main.py__ faili all ja kirjuta __quotes__ järjendisse mitmerealiselt oma lemmiktsitaate. Kui kirjutad ühte ritta kõik,
saad tekstibloki ?quote chatis välja kutsudes.

Testi discordis __?quote__ pannes!

## 🔄 Extra
Kui oled kõik eelnevad ülesanded lahendanud, proovi teha järgmist:
- ⭐ Kui kasutaja sisestab roll_dice, tagasta suvaline arv. Seda saad __response.py__ __get_response__ meetodisse lisada.
<details>
  <summary>Spoiler</summary>

    def get_response(user_input: str) -> str:
        lowered: str = user_input.lower()
        if "roll dice" in lowered:
            return f":game_die: You rolled: {randint(1, 6)}"
        elif lowered in responses.keys():
            return responses[lowered]
</details>

- Tase ⭐ Lisa uus käsk __!delete__ __[@username]__, mida väljakutsudes bot teavitab:"__[@username]__ has been permanently deleted. Goodbye forever. 👋"
- Tase ⭐⭐⭐ meetod, mis salvestab tekstifaili kõik, mida kasutajad sisestavad.