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

Start het script met:

```bash
python main.py
```

### Voorbeelduitvoer

```
=================================================
            Neppe Alias Generator
|-----------------------------------------------|

    Voornaam:        Sjoerd
    Achternaam:      Lange
    Hele naam:       Sjoerd Lange
    Roepnaam:        Hugo
    Geboortedatum:   19-11-1972

|-----------------------------------------------|

    Favoriete kleur: Wit
    Oogkleur:        Hazel

|-----------------------------------------------|

    Postcode:        1566 KN
    Huisnummer:      167
    Plaatsnaam:      Renesse
    Provincie:       Zeeland

=================================================
```

---

## Resultaten

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
├── results/
├──── alias.txt        # gegenereerd
└──── alias.json       # gegenereerd
```

---
