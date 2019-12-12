import csv


heroes = open("menntun_nytt.csv")
reader = csv.DictReader(heroes, delimiter=";")

data = []

for d in reader:
    data.append(d)
heroes.close()

insert_menntun = "Insert into education (year, sex, age, total) values ({}, {}, {}, {}); \n"

f = open('insertstatement_menntun.sql', 'w')


for d in data:
    f.write(insert_menntun.format(d['Ár'], d['Kyn'], d['Aldur'], d['AllirnemendurFjöldinemendaAlls']))

f.close()
