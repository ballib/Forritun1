def position():
    user_input = int(input("Enter a number: "))
    string = ""
    for ch in range(1,10+1):
        if ch == user_input:
            string = string +("o")
        else:
            string = string +("x")
    print(string)

    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
def move():
    mover = input("Input your choice: ")

    if mover == "r":
        return position(user_input=+1)






def main():
    position()




main()