with open('places_provinces.csv', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines[1242:1248], start=1243):
    print(i, repr(line))