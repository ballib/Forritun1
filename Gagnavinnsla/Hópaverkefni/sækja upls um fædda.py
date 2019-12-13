import csv


born = open("FÆDDBÖRNAÐAL.csv", encoding='utf-8')
reader = csv.DictReader(born, delimiter=";")

data = []

for d in reader:
    data.append(d)

born.close()


insert_birthrate = "Insert into birthrate (year, total, under20, age20_24, age25_29, age30_34, age35_39, age40_44, age45_49, over50) values ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}); \n"


f = open('insertstatement_fæddir_aðal.sql', 'w')


for d in data:
    f.write(insert_birthrate.format(d['Ár'], d['Alls lifandi fÆdd bÖrn Alls'], d['Alls lifandi fÆdd bÖrn Innan 20 Ára'], d['Alls lifandi fÆdd bÖrn 20-24 Ára'], d['Alls lifandi FÆdd bÖrn 25-29 Ára'], d['Alls lifandi fædd börn 30-34 ára'], d['Alls lifandi fædd börn 35-39 ára'], d['Alls lifandi fædd börn 40-44 ára'], d['Alls lifandi fædd börn 45-49 ára'], d['Alls lifandi fÆdd bÖrn 50 Ára og eldri']))

f.close()
