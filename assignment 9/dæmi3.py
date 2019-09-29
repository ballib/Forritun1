longest = ''

with open("words.txt", "r", encoding = "utf-8") as text_file:
    for word in text_file:
        strip = word.strip().replace(' ', '')
        if len(strip) > len(longest):
            longest = strip


longest_length = len(longest)


print(word)
print("Longest word is", "'"+str(longest)+"'", "of length", str(longest_length))
