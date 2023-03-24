from datetime import *

pattern = '%d.%m.%Y'

dt = datetime.strptime(input(), pattern)
aa = 7
ddd = {}

for i in range(int(input())):
    a = input()
    c = datetime.strptime(a[-10:], pattern)
    dt2 = c.replace(year=dt.year)
    days = abs(dt - dt2)

    if days.days <= 7:
        if days.days <= 0 :

            aa = days.days
            kk = c

        if c not in ddd:
            ddd[c] = [a[:len(a) - 10]]
        else:
            ddd[c].append(a[:len(a) - 10])
zxcv = max(ddd.keys())
if len(ddd) >0:

    print(*ddd[zxcv])
else:
    print('Дни рождения не планирются')
print(sum([i for i in range(1, 11)]))