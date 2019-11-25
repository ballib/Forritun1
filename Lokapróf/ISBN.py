def check_correct_length(the_string):
    my_list = []

    if len(the_string) == 13:
        for ch in the_string:
            my_list.append(ch)
        return my_list

    else:
        print("Invalid format!")
        main()



def checker(my_list):

    first = my_list[1]
    second = my_list[5]
    third = my_list[-2]

    if first == "-":
        if second == "-":
            if third == "-":
                print("Valid format!")
    else:
        print("Invalid format!")



def main():
    while True:
        the_string = input("Enter an ISBN: ")
        if the_string == "q":
            quit()
        else:
            check_correct_length(the_string)
            my_list = check_correct_length(the_string)
            checker(my_list)







main()