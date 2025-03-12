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

## 🤖 Boti käivitamine
Failis main.py on peamine boti loogika. Kontrolli, kas bot suudab õigesti käivituda ja ühendada serveriga.

Kui kõik on õigesti seadistatud, saad boti käivitada (terminalis alloleva käsuga või vajutades üleval paremal rohelist kolmnurka):
````
python main.py
````
Kui bot ühendub edukalt, peaksid terminalis nägema:

__BotName is now running!__

## 💬 Sõnumite lugemine
Pane bot reageerima sõnumitele __on_message()__ meetodiga __main.py__ failis.

Lisa tingimus, et bot vastaks sõnumitele vaid siis, kui need EI alga küsimärgiga.

Testi discordis küsimärki sisestades!

## 🎲 Märgusõnadele vastamine
Suundu __cogs__ kausta ja sealt leiad faili __quoting.py__. Sinna klassi on vaja lisada __get_response__ meetodi väljakutse ja botile peab klassi Cog objektina ka lisama. 

Seejärel vaata faili __quotes.py__.

1. Loo meetod, mis tagastab juhusliku täringu tulemuse.

2. Nüüd loo meetod, mis annab juhusliku tsitaadi. Selleks pead tsitaate lisama märgusõna ja vastuse sõnastikku __responses__.

Seerjärel on sul vaja __main-py__ failis kasutada __pathlib.Path__ abil kõigi __.py__ failide otsimiseks ja nende laadimiseks load_extension() kaudu, et bot leiaks __cogs__ kasuta.
Testi discordis __?roll__ ja __responses__ sõnastiku võtmeid kirjutades!

## 🐶 ASCII koer
Suundu __cogs__ kausta ja sealt leiad faili __dog.py__. 

1. Kõigepealt kontrolli, kas fail __dog__ eksisteerib ja lisa logimine juhuks, kui fail jääb leidmata.

2. Lisa uus käsk meetodi __create_dog__, mis loeb ASCII-kunsti __dog__ failist.

Testi discordis __?mouse__ pannes!

## 📜 Tsiteerimine
Failist __quotes.py__ leiad tsitaatide loend.

Lisa oma lemmiktsitaadid järjendisse __quotes__.

Testi discordis __?quote__ pannes!

## 🔄 Extra
Kui oled kõik eelnevad ülesanded lahendanud, proovi teha järgmist:
- ⭐ Lisa uus käsk ?ping, mis tagastab boti latentsuse (pingi) millisekundites
- ⭐ Lisa logimine, et bot saaks terminalis logida kõiki käske, mida kasutajad sisestavad
- ⭐ Lisa kasutajate statistikafunktsioon (nt mitu käsku on botilt küsitud)