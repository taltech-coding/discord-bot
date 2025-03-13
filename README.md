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
Rahategemine pole kunagi olnud lihtsam!
Täna proovime kätt nii dicord.py teegi kasutamise, .env faili loomise kui ka cogside abil koodi modulleerimisega.
Ülesannete näidislahendused leiad solutions kaustast!

## Setup
Kõigepealt suundu terminali ja sisesta:
````bash
pip install discord.py python-dotenv
````
Nüüd loo `.env` fail ja määra sinna oma Discordi boti token:
````py
TOKEN=siia_oma_boti_token
````

## 🤖 1. Boti käivitamine
Failis main.py on peamine boti loogika. Kontrolli, kas bot suudab õigesti käivituda ja ühendada serveriga.

Kui kõik on õigesti seadistatud, saad boti käivitada (terminalis alloleva käsuga või vajutades üleval paremal rohelist kolmnurka):
````
python main.py
````
Kui bot ühendub edukalt, peaksid terminalis nägema midagi sellist:

__BotName#1234 is now running!__

## 💬 2. Sõnumite lugemine
Pane bot reageerima sõnumitele kasutades __on_message()__ meetodit __main.py__ failis.

Lisa tingimus, et bot vastaks sõnumitele vaid siis, kui need EI alga küsimärgiga.
Sõnumit saab saata järgneva käsuga: `await message.channel.send(response)`, kus response on näiteks "Hello".

Testi discordis küsimärki sisestades!

## 🎲 3. Märgusõnadele vastamine
Liigu faili __response.py__

1. 

2. Lisa __roll_dice()__ meetodisse õige vahemik (nt on tavlise täringu nmbrite vahemik 1-6)


Seerjärel on sul vaja __main.py__ failis kasutada __pathlib.Path__ abil kõigi __.py__ failide otsimiseks ja nende laadimiseks load_extension() kaudu, et bot leiaks __cogs__ kasuta.
Testi discordis __?roll__ ja __responses__ sõnastiku võtmeid kirjutades!

## 🐶 4. ASCII koer
Suundu __cogs__ kausta ja sealt leiad faili __quoting.py__. 
Kõigepealt lisa `__init__(self, bot)` meetodisse viide botile (selleks et saaks boti kasutada ka siin failis). Vihje: viide botile on `bot`, mis on `__init__` meetodi üks parameetritest.

Suundu __cogs__ kausta ja sealt leiad faili __dog.py__. 

1. Kõigepealt kontrolli, kas fail __dog__ eksisteerib ja lisa logimine juhuks, kui fail jääb leidmata.

2. Lisa uus käsk meetodi __create_dog__, mis loeb ASCII-kunsti __dog__ failist.

Testi discordis __?mouse__ pannes!

## 📜 5. Tsiteerimine
Failist __quotes.py__ leiad tsitaatide loend.

Lisa oma lemmiktsitaadid järjendisse __quotes__.

Testi discordis __?quote__ pannes!

## 🔄 Extra
Kui oled kõik eelnevad ülesanded lahendanud, proovi teha järgmist:
- ⭐ Lisa uus käsk ?ping, mis tagastab boti latentsuse (pingi) millisekundites
- ⭐ Lisa logimine, et bot saaks terminalis logida kõiki käske, mida kasutajad sisestavad
- ⭐ Lisa kasutajate statistikafunktsioon (nt mitu käsku on botilt küsitud)