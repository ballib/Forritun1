import csv
heroes = open("incident_report.csv")

data = []
cost = []


reader = csv.reader(heroes, delimiter="$")


next(reader, None)
for row in reader:
    data.append(row)

    cost.append(row[-1])

cost = [int(i) for i in cost]




print("Total damage: $"+str(sum(cost)))


