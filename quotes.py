from random import choice

"""
TODO 5.1 Lisa quotes järjendisse juurde tsitaate / sõnumeid

Iga tsitaadi vahel peab olema koma ning peavad olema ümbritsetud jutumärkidega. 
Näiteks võib tsitaatide järjend välja näha nii:
["üks", "kaks"]
"""
quotes = [""]

def get_quote():
    return choice(quotes)
