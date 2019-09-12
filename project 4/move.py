pos = int((input("Input a position between 1 and 10: ")))
string = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]

string[pos-1] = "o"


print(*string)

"""
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")
move = input("Input your choice: ")
"""