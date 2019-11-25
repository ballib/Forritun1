def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None



def winning_numbers_to_list():
    my_list = []
    win_num = str(input("Enter winning numbers: "))
    my_list.append([int(x) for x in win_num.strip().split(" ")])
    return my_list




def lotto_to_list(filestream):
    lotto_list = []
    for line in filestream:
        lotto_list.append([int(x) for x in line.strip().split(" ")])
    return lotto_list




def checker(lotto_list, my_list):

    for num1 in lotto_list:
        for num2 in num1:
            if num2 in my_list[0]:
                print(num2, end="* ")
            else:
                print(num2, end=" ")
        print()
    #print(my_list)
    #print(lotto_list)




def main():
    filename = input("Enter file name: ")
    file_stream = open_file(filename)
    if open_file(filename) == None:
        print("File", filename, "not found!")
    else:
        my_list = winning_numbers_to_list()
        lott_list = lotto_to_list(file_stream)
        checker(lott_list, my_list)





main()