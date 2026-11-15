import csv
with open("test.csv") as f:
    r=csv.reader(f)
    print(r)
    print('-----------')
    for i in r:
        print(i)
    f.seek(0)
    d=csv.DictReader(f)
    print(d)
    for i in d:
        print(i)
        print(i['Name'])
    print(d)
    for i in d:
        print(d)
    for j in d:
        print(j["Name"])

print('\n\n--------')
for i in d:
    print(i)
    print(i['Name'])
print(d)
for i in d:
    print(d)
for j in d:
    print(j["Name"])



with open("test.csv") as f:
    d=csv.DictReader(f)
    print(d)
    for i in d:
        print(i)

