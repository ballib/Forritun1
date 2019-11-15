def fibo(n):
    ''' Prints the first n elements of a Fibonacci series'''
    first = 0
    second = 1
    print(second, end=' ')

    for i in range(2,n+1):
        current = first + second
        print(current, end= ' ')
        first = second
        second = current

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
fibo(n)