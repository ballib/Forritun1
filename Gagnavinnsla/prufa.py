import csv
import re

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
    heroes.close()
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



#6: Hvaða hverfi (e. neighborhood) er hættulegast, þ.e. með flest slagsmál?

def neighborhood(data):
    neighborhoods = {}
    for index, value in enumerate(data["Location"]):
        land = value.split(',')[0].strip()
        if land not in neighborhoods:
            neighborhoods[land] = [0]
        neighborhoods[land][0] += 1
    maximum = max(neighborhoods, key=neighborhoods.get)
    mininum = min(neighborhoods, key=neighborhoods.get)
    max_numbers = (neighborhoods[maximum])
    min_numbers = (neighborhoods[mininum])
    return neighborhoods, maximum, mininum, max_numbers, min_numbers



def hells_kitchen(data):
    """
    8: Hvaða ofurhetja tekur þátt í flestum slagsmálum sem gerast í hverfinu Hell's Kitchen?

    8: Most incidents in Hell's Kitchen (31 incidents): Teenage Mutant Ninja Turtles
    :return:
    """
    most = {}
    for index, place in enumerate(data['Location']):
        new_place = place.split(',')[0].strip()
        if new_place == "Hell's Kitchen":
            for person in re.split(', | vs. ', data['Participants'][index]):
                if person not in most:
                    most[person] = 0
                most[person] += 1

    maximum = max(most, key=most.get)
    max_numbers = most[maximum]

    return maximum, max_numbers


def four_member_teams(data):
    teams = {}

    for persons in data['Participants']:
        for team in persons.split(' vs. '):
            if len(team.split(',')) == 4:
                if team not in teams:
                    teams[team] = 0
                teams[team] += 1

    maximum = max(teams, key=teams.get)
    max_value = teams[maximum]
    the_teams = [max_value, []]

    for key, value in teams.items():
        if value == max_value:
            the_teams[1].append(key)
    the_teams = [the_teams[0], '; '.join(sorted(the_teams[1]))]
    return the_teams

def most_teams(data):
    biggest_team = {}
    for persons in data['Participants']:
        for team in persons.split(' vs. '):
            if team not in biggest_team:
                biggest_team[team] = 0
            biggest_team[team] = len(team.split(","))
    biggest_team_max = max(biggest_team, key=biggest_team.get)
    biggest_numbers_max = biggest_team[biggest_team_max]
    return biggest_team_max, biggest_numbers_max

def most_figts(data):
    fights = {}

    for index, place in enumerate(data['Participants']):
        for person in re.split(', | vs. ', data['Participants'][index]):
            if person not in fights:
                fights[person] = 0
            fights[person] += 1
    maximum = max(fights, key=fights.get)
    max_numbers = fights[maximum]

    return maximum, max_numbers, fights

def participant_cost(data):
    participant_cost = {}
    for index, value in enumerate(data["Participants"]):
        for person in re.split(', | vs. ', data['Participants'][index]):
            if person not in participant_cost:
                participant_cost[person] = [0, 0]
            participant_cost[person][0] += 1
            participant_cost[person][1] += data["Cost"][index]

    return participant_cost

def highest_total_damage(participants):
    max_inc2 = None
    for key, value in participants.items():
        cost = value[1]
        if max_inc2 is None:
            max_inc2 = (key, cost)
        if max_inc2[1] <= cost:
            max_inc2 = (key, cost)
    return max_inc2

def average_highest_total_damage(participants):
    max_inc3 = None
    for key, value in participants.items():
        cost = value[1]
        atvik = value[0]
        damage = round(cost / atvik,2)
        if max_inc3 is None:
            max_inc3 = (key, damage)
        if max_inc3[1] <= damage:
            max_inc3 = (key, damage)
    return max_inc3

def no_cost(data):
    min = {}
    for index, cost in enumerate(data['Cost']):
        if cost == 0:
            for person in re.split(', | vs. ', data['Participants'][index]):
                if person not in min:
                    min[person] = 0
                min[person] += 1

    return min

def nocost_fights(min, fights):

    nocost_fights ={}
    for x in min:
        if x in fights:
            damage = min[x]/fights[x]
            new_damage = round(damage*100,2)
            if new_damage not in nocost_fights:
                nocost_fights[x] = new_damage
    maximum2 = max(nocost_fights, key=nocost_fights.get)
    max_numbers2 = nocost_fights[maximum2]

    return maximum2, max_numbers2

def unfair_fights(data):

    my_list = []
    unfair = {}
    for x in data['Participants']:
        for teams in x.split(' vs. '):
            persons = teams.split(', ')
            my_list.append(persons)
    for x in range(0, len(my_list), 2):
        stak1 = my_list[x]
        stak2 = my_list[x+1]
        if len(stak1) > 2 * len(stak2):
            for person in stak1:
                person = person.strip()
                if person in unfair:
                    unfair[person] += 1

                else:
                    unfair[person] = 1
        elif 2*len(stak1) < len(stak2):
            for person in stak2:
                person = person.strip()
                if person in unfair:
                    unfair[person] += 1
                else:
                    unfair[person] = 1
    maximum5 = max(unfair, key=unfair.get)
    max_numbers5 = unfair[maximum5]
    return maximum5, max_numbers5, unfair, my_list


def percentage_unfair(unfair, fights):
    percentage_unfair = dict((k, float(unfair[k])/fights[k]) for k in unfair)
    new_dict = {}
    for key, value in percentage_unfair.items():
        new_dict[key] = round(value*100, 2)

    maximum6 = max(new_dict, key=new_dict.get)
    max_numbers6 = new_dict[maximum6]
    return maximum6, max_numbers6






"""def friends_enemies(my_list):                    Náði ekki alveg að klára, þetta function finnur út hversu oft iron man og avengers berjast, semsagt 71x, Þurfti bara að gera þetta fyrir hina
    new_dict = {}
    for x in range(0, len(my_list), 2):
        stak1 = my_list[x]
        stak2 = my_list[x+1]
        for person in stak1:
            if person == "Avengers" or person == "Iron Man":
                for person2 in stak2:
                    if person2 == "Iron Man" or person2 == "Avengers":
                        if person not in new_dict:      
                            new_dict[person] = 0
                        new_dict[person] += 1

    print(new_dict)
    """
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
    neighborhoods, maximum ,minimum, max_numbers, min_numbers = neighborhood(data)
    print(f'6: Most dangerous neighborhood ({str(max_numbers)[1:-1]} incidents): {maximum}')
    print(f'7: Safest neighborhood ({str(min_numbers)[1:-1]} incidents): {minimum}')
    person, maximum = hells_kitchen(data)
    print(f"8: Most incidents in Hell's Kitchen ({maximum} incidents): {person}")
    teams = four_member_teams(data)
    print(f'9: 4-member teams with most incidents ({teams[0]} incidents): {teams[1]}')
    biggest_team_max, biggest_numbers_max = most_teams(data)
    print(f'10: Largest teams ({biggest_numbers_max} members): {biggest_team_max}')
    maximum, max_numbers, fights = most_figts(data)
    print(f'11: Most fights ({max_numbers}): {maximum}')
    participants = participant_cost(data)
    max_inc2 = highest_total_damage(participants)
    print(f'12: Highest total damage (${max_inc2[1]}): {max_inc2[0]}')
    max_inc3 = average_highest_total_damage(participants)
    print(f'13: Highest average damage per fight (${max_inc3[1]}): {max_inc3[0]}')
    min = no_cost(data)
    maximum2, max_numbers2 = nocost_fights(min,fights)
    print(f'14: Highest percentage of no-cost fights ({max_numbers2}%): {maximum2}')
    maximum5, max_numbers5, unfair, my_list = unfair_fights(data)
    print(f'15: Highest number of unfair fights ({max_numbers5}): {maximum5}')
    maximum6, max_numbers6 = percentage_unfair(unfair,fights)
    print(f'16: Highest percentage of unfair fights ({max_numbers6}%): {maximum6}')
    #friends_enemies(my_list)
    #print(f'17: Highest number of friends that are also enemies (144): Black Panther')
main()