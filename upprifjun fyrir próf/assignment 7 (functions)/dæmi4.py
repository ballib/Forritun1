def is_prime():
    num = int(input("Enter a number: "))

    for i in range(2, num):
        if (num % i) == 0:
            return False
        else:
            return True

def main():
    if is_prime() == True:
        print("Is prime")
    else:
        print("Is not prime")

main()