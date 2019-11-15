def open_file(filename):
    with open(filename, "r") as file:
        my_list = []                        ## byrja á því að setja þetta allt í tómann lista
        for line in file:                   ## bý til for-loop sem skoðar hverja línu í filenum
            my_line = line.strip().split(":") ## bý til nýja línu sem er búinn að taka bil og new line með strip og split sem splittar á milli :
            my_list.append(my_line)             ## appenda þessari nýu línu í my_list
        return my_list

def list_to_dict(my_list):
    my_dict = {}                        ## hérna set ég my_list í dictionary
    for x in range(len(my_list)):         ## bý til forloop sem skoðar lengdina af hverjum lista
        key = my_list[x][0]                 ## set key sem fyrra stakið
        value = my_list[x][1]               ## set value sem annað stakið

        my_dict[key] = value            ## festa keyið við þetta value

    return my_dict


def get_choice(my_dict):
    choice = input("Enter a message:")          ##spyr um input
    choice_list = choice.split()                ## passa að ég geti gert bil á milli inputta
    my_string = ""                              ## bý til tómann streng
    for x in choice_list:                       ## bý til for-loopu sem skoðar inputið mitt sem er x
        for key, value in my_dict.items():      ## skoða hvort þetta x (inputið) sé til sem key í my dictionary
            if x == key:                        ## og ef inputið er sama og key sem er til:
                my_string += my_dict[key]+ " "  ## þá bæti ég við í tóma strenginn því sem valueið er það er sótt með my_dict[key]
    print(my_string)
    return


def main():
    filename = input("Enter name of mapping file: ")   ##sæki nafnið á skránni og geymi það í filename
    my_list = open_file(filename)                       ## set nafnið á skránni í openfile functionið sem skilar mér síðan my_list
    my_dict = list_to_dict(my_list)                     ## set my list síðan í list to dict functionið sem skilar mér síðan dictionariuni mínu
    while True:                                         ## bý til while loopu sem fer af stað ef eftirfarandi er satt:
        the_choice = input("Enter a message:")          ## ef the the choice er jafnt of q:
        if the_choice == "q":
            quit()                                        # þá hætti ég í leiknum
        else:
            get_choice(my_dict)                             ## annars þá set ég my dictionary í get choice functionið 

main()