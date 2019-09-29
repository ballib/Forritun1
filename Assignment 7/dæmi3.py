# The function definition goes here
def in_range(num):
    if 1 < num < 555:
        return True
    else:
        return False
num = int(input("Enter a number: "))

if in_range(num):
    print((num), "is in range")
else:
    print((num), "is outside the range!")
# You call the function here