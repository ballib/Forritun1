
# The main program starts here

def to_list(a_string):
    if ',' in a_string:
        return a_string.split(",")
    elif ' ' in a_string:
        return a_string.split()
    else:
        return [a_string]

the_string = input("Enter the string: ")
the_list = to_list(the_string)
# call your function here
print(the_list)