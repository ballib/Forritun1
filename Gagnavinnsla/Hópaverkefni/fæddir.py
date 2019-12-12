import csv


born = open("fæddir.csv")
reader = csv.DictReader(born, delimiter=";")

data = []

for d in reader:
    data.append(d)
born.close()

insert_Forsja = "Insert into Custody_children (year, age15_44, age15_19, age20_24, age25_29, age30_34, age35_39, age40_44, age45_49) values ({}, {}, {}, {}, {}, {}, {}, {}, {}); \n"

f = open('insertstatement_fæddir.sql', 'w')


for d in data:
    f.write(insert_Forsja.format(d['ár'], d['15-44 ára'], d['15-19  ára'], d['20-24 ára'], d['25-29 ára'], d['30-34 ára'], d['35-39 ára'], d['40-44 ára'], d['45-49 ára']))

f.close()
