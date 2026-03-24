import pandas as pd
import json
import random
import requests

VALID_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

TEMP_MAIL_DOMAINS = [
    "armyspy.com",
    "cuvox.de",
    "dayrep.com",
    "einrot.com",
    "fleckens.hu",
    "gustr.com",
    "jourrapide.com",
    "superrito.com",
    "teleworm.us",
]

names_df = pd.read_csv('namen.csv')
FIRST_NAMES = names_df['voornaam'].tolist()
LAST_NAMES  = names_df['achternaam'].tolist()

friends_df = pd.read_csv('friend_names.csv')
FRIENDS_NAMES = friends_df['roepnaam'].tolist()

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


def generate_temp_mail(first: str, last: str) -> tuple[str, str, str]:
    username = f"{first.lower()}{last.lower()}{random.randint(100, 999)}".replace(' ', '')
    domain   = random.choice(TEMP_MAIL_DOMAINS)
    url      = f"https://www.fakemailgenerator.com/#/{domain}/{username}/"
    return username, domain, url


def generate_person() -> dict:
    first = random.choice(FIRST_NAMES)
    last  = random.choice(LAST_NAMES)
    idx   = random.randrange(len(PLACES))
    place, province = PLACES[idx], PROVINCES[idx]

    username, domain, mail_url = generate_temp_mail(first, last)

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
        "temp_mail":       f"{username}@{domain}",
        "temp_mail_url":   mail_url,
    }


def build_output(p: dict) -> str:
    rows = [
        None,
        ("Voornaam",        p["voornaam"]),
        ("Achternaam",      p["achternaam"]),
        ("Hele naam",       p["hele_naam"]),
        ("Roepnaam",        p["roepnaam"]),
        ("Geboortedatum",   p["geboortedatum"]),
        None,
        ("Favoriete kleur", p["favoriete_kleur"]),
        ("Oogkleur",        p["oogkleur"]),
        None,
        ("Postcode",        p["postcode"]),
        ("Huisnummer",      p["huisnummer"]),
        ("Plaatsnaam",      p["plaatsnaam"]),
        ("Provincie",       p["provincie"]),
        None,
        ("Temp e-mail",     p["temp_mail"]),
        ("Mailbox URL",     p["temp_mail_url"]),
    ]

    content_lines = []
    for row in rows:
        if row is None:
            content_lines.append(None)  # separator placeholder
        else:
            label, value = row
            content_lines.append(f"    {label + ':':<16} {value}")

    title = "Neppe Alias Generator"
    inner_w = max(
        len(title) + 4,
        max(len(line) for line in content_lines if line is not None)
    )
    total_w = inner_w + 2  # +2 for the outer | |

    top        = "=" * total_w
    sep        = "|" + "-" * inner_w + "|"
    title_line = "|" + title.center(inner_w) + "|"

    def content_line(text):
        return "|" + text.ljust(inner_w) + "|"

    lines = [top, title_line]
    for item in content_lines:
        if item is None:
            lines.append(sep)
        else:
            lines.append(content_line(item))
    lines.append(top)

    return "\n".join(lines)


def print_person(p: dict):
    print(build_output(p))

def save_txt(p: dict, path="results/alias.txt"):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(build_output(p) + "\n")

def save_json(p: dict, path="results/alias.json"):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(p, f, ensure_ascii=False, indent=4)


def main():
    person = generate_person()
    print_person(person)
    save_txt(person)
    save_json(person)

if __name__ == "__main__":
    main()
