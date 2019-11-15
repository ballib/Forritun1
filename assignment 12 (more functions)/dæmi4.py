
def merge_lists(L1, L2):
    L3 = L1 + [x for x in L2 if x not in L1]
    L3.sort()
    return L3

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
