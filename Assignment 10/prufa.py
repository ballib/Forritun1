import string

s = input("Input a sentence: ")

l = []

for i in s:
    if i not in l and i != ' ':
        l.append(i)

print("Unique letters: ", l)