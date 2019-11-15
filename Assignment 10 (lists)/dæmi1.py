import string

# Implement a function here
def setn(blabla):
    l = []
    for ch in blabla:
        if ch not in l and ch != " ":
            l.append(ch)
    return l


# Main starts here
sentence = input("Input a sentence: ")
unique_letters = setn(sentence)
# Call the function here
print("Unique letters:", unique_letters)

