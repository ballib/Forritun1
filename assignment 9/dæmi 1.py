with open("test.txt", "r") as file:
    for line in file:
        new=line.strip().replace(" ","")
        print(new, end="")