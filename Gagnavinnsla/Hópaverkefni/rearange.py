import csv

heroes = open("menntun_nytt.csv")

data = {}

reader = csv.reader(heroes, delimiter=";")
for header in reader:
    data[header[0]] = []
    data[header[1]] = []
    data[header[2]] = []
    data[header[3]] = []
    break

for value in reader:
    data['Year'].append(int(value[0]))
    data['Sex'].append(value[1])
    data['Age'].append(value[2])
    data['Total'].append(int(value[3]))



"Headers: Ár, Aldur, Kyn, Menntun"

listi = []
for value in data.items():
    for x in data['Age']:
        listi.append(x)

age_strip = ([i.strip(" ").split(' ára', 1)[0] for i in listi])
data['Age'] = ",".join(age_strip)


for key, value in data.items():
    with open("test_csv.csv", "w", encoding='utf-8', newline="" ) as csv_file:
        fieldnames = ['Year', 'Sex', 'Age', 'Total']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for x in range(len(data['Year'])):
            writer.writerow({'Year': data['Year'][x], 'Sex': data['Sex'][x], 'Age': age_strip[x], 'Total': data['Total'][x]})