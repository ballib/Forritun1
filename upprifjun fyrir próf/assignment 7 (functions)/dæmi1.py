
def find_min():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if num1 < num2:
        return num1
    else:
        return num2




def main():
    mini_num = find_min()
    print(mini_num)




main()