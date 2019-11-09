
def get_floats():
    try:
        a_list = [int(x) for x in input("Enter elements of a list separated by space: ").split(' ')]
        return a_list
    except ValueError:
        print("False")



floats = float(input("Enter scores seperated by space: "))
floating_points = get_floats(floats)
