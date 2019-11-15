n = int(input("Enter the length of the sequence: "))

a = 1
b = 2
c = 3
total = 0
print(a)
print(b)
print(c)
while total < n-3:
    d = a+b+c
    total += 1

    print(d)
    a = b
    b = c
    c = d
