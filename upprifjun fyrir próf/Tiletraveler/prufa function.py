
def tile11():
    print("You can travel: (N)orth.")

    direction = input("Direction: ")
    while direction not in ["n","N"]:
        print("Not a valid direction!")
        direction = input("Direction: ")
    else:
        return tile12()



def tile12():
    print("You can travel: (N)orth or (E)ast or (S)outh.")

    direction = input("Direction: ")
    while direction not in ["n","N","s","S","e","E"]:
        print("Invalid direction")
        direction = input("Direction: ")
    if direction == "n":
        return tile13()
    elif direction == "e":
        return tile22()
    elif direction == "s":
        return tile11()



def tile13():
    print("You can travel: (E)ast or (S)outh.")
    direction = input("Direction: ")
    while direction not in ["s","S","e","E"]:
        print("Invalid direction")
        direction = input("Direction: ")
    if direction == "e":
        return tile23()
    elif direction == "s":
        return tile12()


def tile23():
    print("You can travel: (E)ast or (W)est.")
    direction = input("Direction: ")
    while direction not in ["e", "E","w","W"]:
        print("Invalid direction")
        direction = input("Direction: ")
    if direction == "e":
        return tile33()
    elif direction == "w":
        return tile13()

def tile33():
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")
    while direction not in ["s", "S","w","W"]:
        print("Invalid direction")
        direction = input("Direction: ")
    if direction == "s":
        return tile32()
    elif direction == "w":
        return tile23()


def tile32():
    print("You can travel: (N)orth or (S)outh.")
    direction = input("Direction: ")
    while direction not in ["n", "N","s","S"]:
        print("Invalid direction")
        direction = input("Direction: ")
    if direction == "n":
        return tile33()
    elif direction == "s":
        return tile31()


def tile31():
    print("Victory")

def tile22():
    print("You can travel: (W)est or (S)outh.")
    direction = input("Direction: ")
    while direction not in ["w", "W", "s", "S"]:
        print("Invalid direction")
        direction = input("Direction: ")
    if direction == "w":
        return tile12()
    elif direction == "s":
        return tile21()
def tile21():
    print("You can travel: (S)outh.")
    direction = input("Direction: ")
    while direction not in ["s", "S"]:
        print("Invalid direction")
        direction = input("Direction: ")
    if direction == "s":
        return tile22()


def main():
    tile11()



main()