import csv


heroes = open("Passengers_Keflavik.csv")
reader = csv.DictReader(heroes, delimiter=";")

data = []

for d in reader:
    data.append(d)
heroes.close()

nationality_set = set() #Hérna safna ég öllum nationalities í eitt set, því þetta er sér tafla

for d in data:
    nationality_set.add(d['Nationality']) #adda því hér í set

insert_nationality  = "Insert into nationalities (nationality) values ('{}'); \n"
insert_passengers = "Insert into passengers (nationality, year, month, passengercount) values ('{}', {}, '{}', {}); \n"

f = open('insertstatement.sql', 'w')

for n in nationality_set:
    f.write(insert_nationality.format(n)) ##bæti nationality set orðunum inn í print setninguna

for d in data:
    f.write(insert_passengers.format(d['Nationality'], d['Year'], d['Month'], d['Count']))

f.close()
