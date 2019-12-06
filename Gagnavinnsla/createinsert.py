import csv


heroes = open("education_abroad.csv")
reader = csv.DictReader(heroes, delimiter=";")

data = []

for d in reader:
    data.append(d)
heroes.close()

country_set = set() #Hérna safna ég öllum nationalities í eitt set, því þetta er sér tafla

for d in data:
    country_set.add(d['Country']) #adda því hér í set

study_set = set()

for d in data:
    study_set.add(d['Study'])


insert_country  = "Insert into countries (country) values ('{}'); \n"
insert_study = "Insert into studies (study) values ('{}'); \n "
insert_students = "Insert into students (country, study, year, female, male) values ('{}', '{}', ''{}, {}, {}); \n"

f = open('insertstatements.sql', 'w')

for n in country_set:
    f.write(insert_country.format(n)) ##bæti nationality set orðunum inn í print setninguna

for x in study_set:
    f.write(insert_study.format(x))

for d in data:
    f.write(insert_students.format(d['Country'], d['Study'], d['Year'], d['Female'], d['Male']))

f.close()
