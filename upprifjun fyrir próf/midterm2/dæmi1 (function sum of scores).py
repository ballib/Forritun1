def get_floats():
    try:
        a_list = [float(x) for x in input("Enter elements of a list separated by space: ").split(' ')]
        if len(a_list) > 2:
            return a_list
        else:
            raise ValueError
    except ValueError:
        print("At least two scores needed!")
        quit()


def summerize(a_list):
    smallest_number = min(a_list)
    a_list.remove(smallest_number)
    smallest_number2 = min(a_list)
    a_list.remove(smallest_number2)
    the_sum = sum(a_list)
    print("Sum of scores (two lowest removed):",the_sum)






def main():
    a_list = get_floats()
    summerize(a_list)


main()
