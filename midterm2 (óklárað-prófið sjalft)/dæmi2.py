def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        return False


def count_words(fileobject):
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
    return count


filename = input("Enter filename: ")
fileobject = open_file(filename)
if fileobject:
    counted_words = count_words(fileobject)
    print(counted_words)
else:
    print("File", filename, "not found!")

