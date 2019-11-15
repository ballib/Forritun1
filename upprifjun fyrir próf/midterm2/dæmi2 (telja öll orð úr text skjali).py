def open_file(filename):
    try:
        fileobject = open(filename, "r")
        return fileobject
    except FileNotFoundError:
        print("File",filename,"not found!")

def stripper(fileobject):
    count = 0
    word_list = []
    for line_str in fileobject:
        for ch in line_str:
            if ch == "," or ch == "!" or ch == "." or ch == "?":
                count +=1
        line_list = line_str.split(" ")
        for word in line_list:
            word_list.append(word)
            count += 1
            print(word_list)
    return count





def main():
    filename = input("Enter filename: ")
    fileobject = open_file(filename)
    if fileobject:
        counted_words = stripper(fileobject)
        print(counted_words)
    else:
        print("File", filename, "not found!")





main()