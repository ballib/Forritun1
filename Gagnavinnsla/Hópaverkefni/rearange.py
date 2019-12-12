import csv

heroes = open("menntun.csv")

data = {}

reader = csv.reader(heroes, delimiter=";")
for header in reader:
    data[header[0]] = []
    data[header[1]] = []
    data[header[2]] = []
    data[header[3]] = []
    data[header[4]] = []
    data[header[5]] = []
    data[header[6]] = []
    data[header[7]] = []
    data[header[8]] = []
    data[header[9]] = []
    data[header[10]] = []
    data[header[11]] = []
    break

for value in reader:
    data['Kyn'].append(value[0])
    data['Aldursflokkur/búseta'].append(value[1])
    data['Menntun'].append(value[2])
    data['2003'].append(int(value[3]))
    data['2004'].append(int(value[4]))
    data['2005'].append(int(value[5]))
    data['2006'].append(int(value[6]))
    data['2007'].append(int(value[7]))
    data['2008'].append(int(value[8]))
    data['2009'].append(int(value[9]))
    data['2010'].append(int(value[10]))
    data['2011'].append(int(value[11]))


"Headers: Ár, Aldur, Kyn, Menntun"
for value in data.items():
    print(value)

