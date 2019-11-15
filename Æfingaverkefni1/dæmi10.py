num = int(input("Enter a integer: "))
if num < 10 and num > 0:
    print("Less than 10")
elif num >= 10 and num < 20:
    print("between 10 and 20")
elif num >= 20:
    print("the value is too high!")
else:
    print("too low")