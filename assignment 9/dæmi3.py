def open_file(filename):
    file_object = open(filename, "r")
    return file_object

def longest(file_object):
    longest_word = ''
    for word in file_object:
        strip = word.strip().replace(' ', '')
        if len(strip) > len(longest_word):
            longest_word = strip
    return longest_word

def main():
    filename = input("Enter filename: ")
    file_object = open_file(filename)
    longest_word = longest(file_object)
    print("Longest word is",longest_word, "of length", len(longest_word))



main()