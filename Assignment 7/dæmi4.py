# is_prime function definition goes here
def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
        else:
            return True
num = int(input("Input an integer greater than 1: "))

if is_prime(num):
    print((num), "is a prime")
else:
    print((num), "is not a prime")
# Call the function here and print out the appropriate message

## Python program to check if the input number is prime or not

