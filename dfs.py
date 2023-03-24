import csv

d = {}
lp = []
with open('titanic.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    next(rows)
    for l, district, male, count in rows:
        if int(l) == 1 and float(count) < 18.0 and male == 'male':
            lp.append(district)
    for l, district, male, count in rows:
        if int(l) == 1 and float(count) < 18.0 and male == 'female':
            lp.append(district)

with open('titanic.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    next(rows)
    for l, district, male, count in rows:
        if int(l) == 1 and float(count) < 18.0 and male == 'female':
            lp.append(district)

for r in lp:
    print(r)
