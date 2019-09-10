a_str = input("Enter last name, first name: ")
name = a_str.split(","+" ")
fname = name[1]
fletter = fname[0]
lname = name[0]
print(fletter.capitalize()+'.',lname.capitalize())