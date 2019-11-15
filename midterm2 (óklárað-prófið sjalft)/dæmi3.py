def get_numbers():
    try:
        a_list = [int(x) for x in input("Enter elements of a list separated by space: ").split(' ')]
        sort = a_list[:]
        list_sorted = sorted(sort)
        return list_sorted
    except ValueError:
        print("False")


def get_numbers2():
    try:
        a_list = [int(x) for x in input("Enter elements of a list separated by space: ").split(' ')]
        sort = a_list[:]
        list_sorted = sorted(sort)
        return list_sorted
    except ValueError:
        print("False")

def intersection(listi,listi2):
    new_list = listi + listi2
    return new_list



def union(listi,listi2):
    new_list = listi + listi2
    sort = new_list[:]
    list_sorted = sorted(sort)
    return list_sorted



listi = get_numbers()
listi2 = get_numbers2()
listi3 = intersection(listi,listi2)
listi4 = union(listi,listi2)



print("Set 1:", listi)
print("Set 2:", listi2)
print("Intersection: ", listi3)
print("Union: ", listi4)