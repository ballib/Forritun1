import string
def find_unique(wordlist):
    unique = []


    for word in wordlist:
        if word not in unique:
            unique.append(word)
    return unique

def build_wordlist(filestream):
    word_list = []

    for line in filestream:
        wordlist = line.strip().split()
        for word in wordlist:
            word = word.strip(string.punctuation)
            word_list.append(word)
    return word_list





def main():
    filename = input("Enter filename: ")
    file_stream = open(filename)
    word_list = build_wordlist(file_stream)
    file_stream.close()
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()