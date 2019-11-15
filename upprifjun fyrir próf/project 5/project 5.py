def open_file(filename):
    fileobject = open(filename, "r")
    for line in fileobject:
        new_file = line
        print(new_file, end="")


def main():
    filename = input("Enter name of file: ")
    open_file(filename)


main()