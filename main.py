import pandas as pd
from random import randint
from datetime import date
import random
import json

VALID_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

names_df = pd.read_csv('namen.csv')

# Read raw lines and only keep rows with exactly 2 comma-separated fields
with open('places_provinces.csv', encoding='utf-8') as f:
    lines = f.readlines()

header = lines[0].strip().split(',')
rows = []
for line in lines[1:]:
    parts = line.strip().split(',')
    if len(parts) == 2:
        rows.append(parts)
    elif len(parts) == 3:
        # e.g. "Nes,Ameland,Fryslân" → "Nes (Ameland),Fryslân"
        rows.append([f"{parts[0]} ({parts[1]})", parts[2]])

places_provinces_df = pd.DataFrame(rows, columns=header)

FIRST_NAMES = names_df['voornaam'].to_list()
LAST_NAMES = names_df['achternaam'].to_list()
FIRST_NAMES_LENGTH = len(FIRST_NAMES)
LAST_NAMES_LENGTH = len(LAST_NAMES)

PLACES = places_provinces_df['plaatsnaam'].to_list()
PROVINCES = places_provinces_df['provincie'].to_list()
PLACES_LENGTH = len(PLACES)


def random_date(start_year=1900, end_year=None):
    if end_year is None:
        end_year = date.today().year

    year  = randint(start_year, end_year)
    month = randint(1, 12)

    if month == 2:
        day = randint(1, 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28)
    elif month in {4, 6, 9, 11}:
        day = randint(1, 30)
    else:
        day = randint(1, 31)

    return f"{day}-{month}-{year}"


def random_nl_postcode() -> str:
    number = random.randint(1000, 9999)
    letters = ''.join(random.choice(VALID_LETTERS) for _ in range(2))
    return f"{number:04d} {letters}"


def date_of_birth_gen():
    return random_date(1960, 2000)


def random_color(choices: list):
    return choices[randint(0, len(choices) - 1)]


def random_place_province():
    index = randint(0, PLACES_LENGTH - 1)
    return PLACES[index], PROVINCES[index]


def generate_person() -> dict:
    first_name = FIRST_NAMES[randint(0, FIRST_NAMES_LENGTH - 1)]
    last_name  = LAST_NAMES[randint(0, LAST_NAMES_LENGTH - 1)]
    name       = f"{first_name} {last_name}"
    dob        = date_of_birth_gen()
    zip_code   = random_nl_postcode()
    house_number = str(randint(1, 200))
    place, province = random_place_province()

    eye_color = random_color(['Blauw', 'Bruin', 'Groen', 'Hazel'])
    fav_color = random_color([
        'Blauw', 'Rood', 'Geel', 'Groen',
        'Wit', 'Zwart', 'Grijs', 'Oranje'
    ])

    return {
        "voornaam":        first_name,
        "achternaam":      last_name,
        "hele_naam":       name,
        "geboortedatum":   dob,
        "favoriete_kleur": fav_color,
        "oogkleur":        eye_color,
        "postcode":        zip_code,
        "huisnummer":      house_number,
        "plaatsnaam":      place,
        "provincie":       province,
    }


def print_person(p: dict):
    print(f"""
=================================================
            Neppe Alias Generator
|-----------------------------------------------|

    Voornaam:        {p['voornaam']}
    Achternaam:      {p['achternaam']}
    Hele naam:       {p['hele_naam']}
    Geboortedatum:   {p['geboortedatum']}

|-----------------------------------------------|

    Favoriete kleur: {p['favoriete_kleur']}
    Oogkleur:        {p['oogkleur']}

|-----------------------------------------------|

    Postcode:        {p['postcode']}
    Huisnummer:      {p['huisnummer']}
    Plaatsnaam:      {p['plaatsnaam']}
    Provincie:       {p['provincie']}

=================================================
    """)


def save_txt(p: dict, filename: str = "alias.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=================================================\n")
        f.write("            Neppe Alias Generator\n")
        f.write("|-----------------------------------------------|\n\n")
        f.write(f"    Voornaam:        {p['voornaam']}\n")
        f.write(f"    Achternaam:      {p['achternaam']}\n")
        f.write(f"    Hele naam:       {p['hele_naam']}\n")
        f.write(f"    Geboortedatum:   {p['geboortedatum']}\n\n")
        f.write("|-----------------------------------------------|\n\n")
        f.write(f"    Favoriete kleur: {p['favoriete_kleur']}\n")
        f.write(f"    Oogkleur:        {p['oogkleur']}\n\n")
        f.write("|-----------------------------------------------|\n\n")
        f.write(f"    Postcode:        {p['postcode']}\n")
        f.write(f"    Huisnummer:      {p['huisnummer']}\n")
        f.write(f"    Plaatsnaam:      {p['plaatsnaam']}\n")
        f.write(f"    Provincie:       {p['provincie']}\n\n")
        f.write("=================================================\n")

def save_json(p: dict, filename: str = "alias.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(p, f, ensure_ascii=False, indent=4)

def main():
    person = generate_person()
    print_person(person)
    save_txt(person)
    save_json(person)


main()