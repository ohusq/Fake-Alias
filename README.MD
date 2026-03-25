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

- Python 3.14+
- pandas

Installeer de dependencies met:

```bash
python -m pip install -r requirements.txt
```

---

## Gebruik

Start het script met:

```bash
python main.py
```

### Voorbeelduitvoer

```
===========================================================================================
|                                  Neppe Alias Generator                                  |
|-----------------------------------------------------------------------------------------|
|    Voornaam:        Willemijn                                                           |
|    Achternaam:      De Bruin                                                            |
|    Hele naam:       Willemijn De Bruin                                                  |
|    Roepnaam:        Yvette                                                              |
|    Geboortedatum:   6-10-1961                                                           |
|-----------------------------------------------------------------------------------------|
|    Favoriete kleur: Rood                                                                |
|    Oogkleur:        Hazel                                                               |
|-----------------------------------------------------------------------------------------|
|    Postcode:        6845 HV                                                             |
|    Huisnummer:      100                                                                 |
|    Plaatsnaam:      Cadier en Keer                                                      |
|    Provincie:       Limburg                                                             |
|-----------------------------------------------------------------------------------------|
|    Temp e-mail:     willemijndebruin781@fleckens.hu                                     |
|    Mailbox URL:     https://www.fakemailgenerator.com/#/fleckens.hu/willemijndebruin781/|
===========================================================================================
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
├── friend_names.csv
├── results/
├──── alias.txt        # gegenereerd
└──── alias.json       # gegenereerd
```

---
