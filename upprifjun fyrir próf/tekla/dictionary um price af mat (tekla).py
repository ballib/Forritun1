def get_price_for_product(product_name):
    prices = {
        'egg': 0.25,
        'milk': 0.75,
        'bread': 3.5,
        'beef': 25.50,
        'tomatoes': 0.15,
        'lettuce': 2,
        'apple': 0.40
    }

    return prices[product_name]

def open_file(filename):
    try:
        with open(filename, "r") as my_data:
            my_list = []
            for line in my_data:
                my_line = line.replace("\n", "").split(",")
                my_list.append(my_line)
            return my_list
    except FileNotFoundError:
        print("File not found")
        quit()

def find_price(my_list):
    my_dict = {}
    for x in range(len(my_list)):
        person = my_list[x][0]
        price_of_product = get_price_for_product(my_list[x][1])
        quantity = float(my_list[x][2])

        price = price_of_product * quantity
        if person not in my_dict:
            my_dict[person] = price
        else:
            my_dict[person] += price
    for key, value in my_dict.items():
        print("{} spent {:.2f}$".format(key, value))


def main():
    filename = input("Enter the name of the file: ")
    my_list = open_file(filename)
    find_price(my_list)

main()