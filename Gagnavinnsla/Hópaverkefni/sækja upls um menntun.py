import csv


heroes = open("menntun.csv")
reader = csv.DictReader(heroes, delimiter=";")

data = []

for d in reader:
    data.append(d)
heroes.close()

insert_menntun = "Insert into education (sex, age_group, education, year_2003, year_2004, year_2005, year_2006, year_2007, year_2008, year_2009, year_2010, year_2011) values ('{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}); \n"

f = open('insertstatement_menntun.sql', 'w')


for d in data:
    f.write(insert_menntun.format(d['Kyn'], d['Aldursflokkur/búseta'], d['Menntun'], d['2003'], d['2004'], d['2005'], d['2006'], d['2007'], d['2008'], d['2009'], d['2010'], d['2011']))

f.close()
