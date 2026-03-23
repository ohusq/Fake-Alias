import pandas as pd
import json
import random
import requests

VALID_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

FRIENDS_NAMES = ["Ace", "Buddy", "Chief", "Duke", "Flash", "Ghost", "Hawk", "Ice"]

names_df = pd.read_csv('namen.csv')
FIRST_NAMES = names_df['voornaam'].tolist()
LAST_NAMES  = names_df['achternaam'].tolist()

with open('places_provinces.csv', encoding='utf-8') as f:
    lines = f.readlines()

header = lines[0].strip().split(',')
rows = []
for line in lines[1:]:
    parts = line.strip().split(',')
    if len(parts) == 2:
        rows.append(parts)
    elif len(parts) == 3:
        rows.append([f"{parts[0]} ({parts[1]})", parts[2]])

places_provinces_df = pd.DataFrame(rows, columns=header)
PLACES    = places_provinces_df['plaatsnaam'].tolist()
PROVINCES = places_provinces_df['provincie'].tolist()


def random_date(start=1960, end=2000):
    y = random.randint(start, end)
    m = random.randint(1, 12)
    if m == 2:
        d = random.randint(1, 29 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 28)
    elif m in {4, 6, 9, 11}:
        d = random.randint(1, 30)
    else:
        d = random.randint(1, 31)
    return f"{d}-{m}-{y}"


def lookup_postcode(city: str) -> str | None:
    try:
        r = requests.get(
            "https://gratis-postcodedata.nl/api/suggest",
            params={"q": city, "country": "nl", "limit": 10}, timeout=5
        )
        r.raise_for_status()
        results = r.json().get("results", [])
        matches = [x for x in results if x.get("plaats", "").lower() == city.lower()] or results
        if matches:
            raw = random.choice(matches)["postcode"]
            return f"{raw[:4]} {raw[4:]}"
    except Exception:
        pass
    return None


def random_postcode() -> str:
    return f"{random.randint(1000, 9999):04d} {''.join(random.choices(VALID_LETTERS, k=2))}"


def generate_person() -> dict:
    first = random.choice(FIRST_NAMES)
    last  = random.choice(LAST_NAMES)
    idx   = random.randrange(len(PLACES))
    place, province = PLACES[idx], PROVINCES[idx]

    return {
        "voornaam":        first,
        "achternaam":      last,
        "hele_naam":       f"{first} {last}",
        "roepnaam":        random.choice(FRIENDS_NAMES),
        "geboortedatum":   random_date(),
        "favoriete_kleur": random.choice(['Blauw', 'Rood', 'Geel', 'Groen', 'Wit', 'Zwart', 'Grijs', 'Oranje']),
        "oogkleur":        random.choice(['Blauw', 'Bruin', 'Groen', 'Hazel']),
        "postcode":        lookup_postcode(place) or random_postcode(),
        "huisnummer":      str(random.randint(1, 200)),
        "plaatsnaam":      place,
        "provincie":       province,
    }


TEMPLATE = """\
=================================================
            Neppe Alias Generator
|-----------------------------------------------|

    Voornaam:        {voornaam}
    Achternaam:      {achternaam}
    Hele naam:       {hele_naam}
    Roepnaam:        {roepnaam}
    Geboortedatum:   {geboortedatum}

|-----------------------------------------------|

    Favoriete kleur: {favoriete_kleur}
    Oogkleur:        {oogkleur}

|-----------------------------------------------|

    Postcode:        {postcode}
    Huisnummer:      {huisnummer}
    Plaatsnaam:      {plaatsnaam}
    Provincie:       {provincie}

================================================="""


def print_person(p: dict):
    print(TEMPLATE.format(**p))

def save_txt(p: dict, path="results/alias.txt"):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(TEMPLATE.format(**p) + "\n")

def save_json(p: dict, path="results/alias.json"):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(p, f, ensure_ascii=False, indent=4)


def main():
    person = generate_person()
    print_person(person)
    save_txt(person)
    save_json(person)

main()