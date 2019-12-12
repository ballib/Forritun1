import csv


born = open("test_csv.csv")
reader = csv.DictReader(born, delimiter=",")

data = []

for d in reader:
    data.append(d)

born.close()

year_set = set()
for d in data:
    year_set.add(d['Year'])
insert_year  = "Insert into years (year) values ({}); \n"
insert_menntun = "Insert into education (year, sex, age, total) values ({}, '{}', {}, {}); \n"


f = open('insertstatement_menntun.sql', 'w')
for n in year_set:
    f.write(insert_year .format(n))

for d in data:
    f.write(insert_menntun.format(d['Year'], d['Sex'], d['Age'], d['Total']))

f.close()
