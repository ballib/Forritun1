for x in range(10, 100):
    a = x // 10
    b = x % 10
    total = (a + b)**2
    if total == x:
        print(x)
    x += 1

for i in range(1,100):
    count = 0
    for x in range(1,i+1):
        if i % x == 0:
            count += 1
    if count == 10:
        print(i)
