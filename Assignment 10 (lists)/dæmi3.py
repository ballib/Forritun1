# Your functions should appear here
def add_to_list(blabla):
    while True:
        strengur = input("Enter value to be added to list: ")
        if strengur.lower() == "exit":
            break
        else:
            blabla.append(strengur)
    else:
        return blabla


def copy(strengur):
    return strengur *3



# Main program starts here
initial_list = []
add_to_list(initial_list)
new_list = copy(initial_list)

for items in new_list:
    print(items)

# It should mostly be a sequence of function calls
