pos = int((input("Input a position between 1 and 10: ")))
move1 = "r"

def position(i):
    empty_string = ""
    for x in range(1, 10+1):
        if x == i:
            empty_string = empty_string + ("o")
        else:
            empty_string = empty_string + ("x")
    print(empty_string)

def move(y):
    global pos
    if y == ("r") and pos < 10:
        pos = pos + 1

    if y == ("l") and pos > 1:
        pos = pos - 1

    position(pos)
position(pos)
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")

while move1 == "r" or move1 == "l":
    move1 = input("Input your choice: ")
    move(move1)
