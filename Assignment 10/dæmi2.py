
# The main program starts here

def to_list(string):
    l = list(string.split(" "))
    l = list(string.split(","))
    return l

the_string = input("Enter the string: ")
the_list = to_list(the_string)
# call your function here
print(the_list)