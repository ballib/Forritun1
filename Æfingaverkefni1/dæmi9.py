a = int(input("Enter a integer: "))
b = int(input("Enter another integer: "))
c = int(input("Enter another integer: "))

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)
    