
def open_file():

    my_dict = {}

    with open("flights.txt", "r") as file:
        for line in file:
            (key, val) = line.split()     ## skiptist á línu fyrir key og value
            if key not in my_dict:        ## ef key er ekki í my_dict
                my_dict[key] = []         ## ef t.d.  keyinn john er ekki til í my_dict þá setjum við hann þar inn
            my_dict[key].append(val)       ## hérna bæti ég value við þann key í þennan tóma lista sem fylgir keyinu
    return my_dict

def organize(lists):
    for word in sorted(lists):                     ## hér bý ég til for-loopu sem prentar út hvert orð í dictionaryinu en þar sem þetta er dictionary þá prentast bara út keys.
        print(word+":")
        for country in sorted(set(lists[word])):            ##  hér prenta ég út value fyrir hvert orð.
            print("\t"+country)

def most_countries(lists):
    max_user = None
    for word in set(lists):
        if max_user is None:
            max_user = (word, len(set(lists[word])))
        if int(max_user[1]) <= len(set(lists[word])):
            max_user = (word, len(set(lists[word])))

    return max_user


def main():
    lists = open_file()
    organize(lists)
    most_countries(lists)
    max_user = most_countries(lists)
    print(f"{max_user[0]} has been to {max_user[1]} countries")







main()