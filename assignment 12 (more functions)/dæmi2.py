# sort_list() function goes here
def sort_list(a_list):
    a_list.sort()


# get_list() function goes here
def get_list():
    a_list = []
    while True:
        try:
            num = int(input())
            a_list.append(num)
        except:
            break
    return a_list



# Do not modify this part
def main():
    a_list = get_list()
    print(a_list)
    print(sort_list(a_list))
    print(a_list)


main()