def count_case():
    string = input("Enter a string: ")
    upper = 0
    lower = 0
    for ch in string:
        if ch.islower():
            lower += 1
        else:
            upper +=1
    print("Upper case count: ",upper)
    print("Lower case count: ",lower)


def main():
    count_case()







main()