import csv


def open_file():
    heroes = open("incident_report.csv")

    data = {}

    reader = csv.reader(heroes, delimiter=";")
    for header in reader:
        data[header[0]] = []
        data[header[1]] = []
        data[header[2]] = []
        break
    for value in reader:
        data['Location'].append(value[0])
        data['Participants'].append(value[1])
        data['Cost'].append(int(value[2].replace('$', '')))

    return data


def total_damage(data):
    return sum(data['Cost'])

def no_harm(data):
    no_harm = 0
    harm = 0

    for value in data["Cost"]:
        if value == 0:
            no_harm += 1
        else:
            harm += 1

    x = no_harm + harm
    percentage = no_harm / x
    return percentage*100

def high_cost(data):
    high_cost = 0

    for value in data["Cost"]:
        if value >= 100000:
            high_cost +=1
    return high_cost


def borough(data):
    borough = {}
    for index, value in enumerate(data["Location"]):
        land = value.split(',')[1].strip()
        if land not in borough:
            borough[land] = [0, 0]
        borough[land][0] += 1
        borough[land][1] += data["Cost"][index]

    return borough


def damage_per_incident(borough):

    max_inc = None
    for key, value in borough.items():
        cost = value[1]
        atvik = value[0]
        damage = round(cost / atvik,2)
        if max_inc is None:
            max_inc = (key, damage)
        if max_inc[1] <= damage:
            max_inc = (key, damage)
    return max_inc









def main():
    data = open_file()
    print(f"1: Total damage: ${total_damage(data)}")
    print(f"2: Percentage of no-cost incidents: {no_harm(data)}%")
    print(f"3: Number of high-cost incidents: {high_cost(data)}")
    print(f"4: Borough overview, by total damage:")
    boroughs = borough(data)
    sorted_dic = sorted(boroughs.items(), key=lambda v: v[1][0])
    for x in sorted_dic[::-1]:
        print(f'\t{x[0]}: {x[1][0]} (${x[1][1]})')
    max_inc = damage_per_incident(boroughs)
    print(f"5: Borough with highest damage per incident (${max_inc[1]}): {max_inc[0]}")


main()