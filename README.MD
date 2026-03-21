# Fake Alias Generator

Een Python script dat willekeurige Nederlandse nep identiteiten genereert op basis van echte voor en achternamen, plaatsnamen en provincies.

---

## Wat doet het?

Het script genereert een willekeurige neppe alias met de volgende gegevens:

- Voor + achternaam
- Geboortedatum
- Favoriete kleur en oogkleur
- Nederlandse postcode en huisnummer
- Plaatsnaam en provincie

De uitvoer wordt getoond in de terminal en opgeslagen als `alias.txt` en `alias.json`.

---

## Vereisten

- Python 3.8+
- pandas

Installeer de dependencies met:

```bash
pip install pandas
```

---

## Gebruik

Zorg dat de volgende bestanden in dezelfde map staan als `main.py`:

- `namen.csv` met kolommen `voornaam` en `achternaam`
- `places_provinces.csv` met kolommen `plaatsnaam` en `provincie`

Start het script met:

```bash
python main.py
```

### Voorbeelduitvoer

```
=================================================
            Neppe Alias Generator
|-----------------------------------------------|

    Voornaam:        Martijn
    Achternaam:      Van Dijk
    Hele naam:       Martijn Van Dijk
    Geboortedatum:   1-2-1988

|-----------------------------------------------|

    Favoriete kleur: Groen
    Oogkleur:        Blauw

|-----------------------------------------------|

    Postcode:        9798 PA
    Huisnummer:      159
    Plaatsnaam:      Garmerwolde
    Provincie:       Groningen

=================================================
```

---

## Uitvoerbestanden

| Bestand | Inhoud |
|---|---|
| `alias.txt` | Opgemaakte tekstversie van de alias |
| `alias.json` | Alle velden als JSON object |

---

## Projectstructuur

```
Fake Alias/
├── main.py
├── namen.csv
├── places_provinces.csv
├── alias.txt        # gegenereerd
└── alias.json       # gegenereerd
```

---