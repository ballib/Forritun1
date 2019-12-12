import csv


heroes = open("Forsjabarna.csv")
reader = csv.DictReader(heroes, delimiter=";")

data = []

for d in reader:
    data.append(d)
heroes.close()

insert_Forsja = "Insert into Custody_children (year, total_children, mother_custody, father_custody, common_custody, not_known) values ({}, {}, {}, {}, {}, {}); \n"

f = open('insertstatement_forsjabarna.sql', 'w')


for d in data:
    f.write(insert_Forsja.format(d['Ár'], d['Börn Alls'], d['Móðir með forsjá'], d['Faðir með forsjá'], d['Sameiginleg forsjá'], d['Aðrir fá forsjá eða ótilgreint']))

f.close()
