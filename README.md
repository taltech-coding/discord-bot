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
Täna proovime kätt nii discord.py teegi kasutamise, .env faili loomise kui ka cogs'ide abil koodi modulleerimisega.
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

Testi discordis küsimärki sisestades (nt ?help)!

## 🎲 3. Märgusõnadele vastamine
Liigu faili __response.py__

1. Lisa __main.py__ faili __on_message()__ meetodi alla response'i saamine ning vastuse saatmine.
2. Liigu __response.py__ faili ning lisa responses muutujasse uued commandid ja vastused.
3. Saada tagasi õige vastus kasutaja sisendile __get_response()__ meetodis.

4. Lisa __roll_dice()__ meetodis õige vahemik (nt on tavalise täringu numbrite vahemik 1-6).


<!-- Seerjärel on sul vaja __main.py__ failis kasutada __pathlib.Path__ abil kõigi __.py__ failide otsimiseks ja nende laadimiseks load_extension() kaudu, et bot leiaks __cogs__ kasuta.
Testi discordis __?roll__ ja __responses__ sõnastiku võtmeid kirjutades! -->

## 🐶 4. ASCII koer
<!-- Suundu __cogs__ kausta ja sealt leiad faili __quoting.py__.  -->


Suundu __cogs__ kausta ja sealt leiad faili __dog.py__. 

1. Kõigepealt lisa `__init__(self, bot)` meetodisse viide botile (selleks et saaks boti kasutada ka __dog.py__ failis). Vihje: viide botile on `bot`, mis on `__init__` meetodi üks parameetritest (parameeter on sulgude sees).
2. Kontrolli, kas fail __dog__ eksisteerib (see peaks olema samas kaustas kus __main.py__).
3. Lisa õige faili nimi, loe andmeid failist ning saada tagasi ASCII pilt koerast. 


Testi discordis __?mouse__ pannes (või see mis sa käsu nimeks panid)!

## 📜 5. Tsiteerimine
Failist __quotes.py__ leiad tsitaatide loendi.

1. Lisa oma lemmiktsitaadid järjendisse __quotes__.
2. Mine __cogs__ kausta __quoting.py__ faili ning lisa viide botile `__init__(self, bot)` meetodis.
3. Saada botiga suvaline tsitaat kasutades `get_quote()` meetodit. Sõnumi saatmine oli täpsemini kirjas neljandas ülesandes.
4. Lisa funktsiooni registreerimine `setup()` meetodis. Vaata kuidas __dog.py__ failis `setup()` tehtud on (ning asenda `Dog` objekt `Quotes` objektiga)

Testi discordis __?quote__ pannes!

## 🔄 Extra
Kui oled kõik eelnevad ülesanded lahendanud, proovi teha järgmist:
- ⭐ Lisa uus käsk ?ping, mis tagastab boti latentsuse (pingi) millisekundites
- ⭐ Lisa logimine, et bot saaks terminalis logida kõiki käske, mida kasutajad sisestavad
- ⭐ Lisa kasutajate statistikafunktsioon (nt mitu käsku on botilt küsitud)