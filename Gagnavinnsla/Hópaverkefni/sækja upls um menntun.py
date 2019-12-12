import csv


born = open("test_csv.csv")
reader = csv.DictReader(born, delimiter=";")

data = []

for d in reader:
    data.append(d)
born.close()
insert_menntun = "Insert into education (year, sex, age, total) values ({}, {}, {}, {}); \n"

f = open('insertstatement_menntun.sql', 'w')


for d in data:
    f.write(insert_menntun.format(d['Year'], d['Sex'], d['Age'], d['Total']))

f.close()
