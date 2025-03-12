## Response.py

### staatiline sõnastik

The random.choice() meetod valib juhusliku elemendi, seda võib kasutada ka listi, tuple'i või stringi peal.
```py
from random import randint
```

__responses__ on sõnastik. Ehk kui kasutaja kirjutab järgnevad sõnad (sõnad, mitte käsud), siis Bot vastab võtme väärtusega ehk reaga teiselpool kooloni.
```py
responses = {
    "skibidi": ":musical_note: Skibidi bop, yes!",
    "yeet": ":rocket: Yeet it to the moon!",
    "brain rot": ":brain: This is peak brain rot.",
    "flex": ":muscle: Flex on 'em!",
    "slay": ":fire: Slay, queen!",
    "drip": ":droplet: Drip too hard!",
    "cap": ":skull: No cap, this is serious.",
    "sigma": ":sunglasses: Sigma grindset activated.",
    "rizz": ":fire: Rizz king/queen in action!"
}
```


### kasutaja sõnumi haldamine

Loeme kasutaja sõnumis kõiki tähti väiketähtedena ning tagastame suvalise arvu "roll dice" sõnumi puhul. 
Kui kasutaja sõnum (sõnum, mitte üksik sõna sõnumist) leidub meie sõnastiku võtmete seas, tagastame võtme väärtuse.
```py
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if "roll dice" in lowered:
        return f":game_die: You rolled: {randint(1, 6)}"
    elif lowered in responses.keys():
        return responses[lowered]
```