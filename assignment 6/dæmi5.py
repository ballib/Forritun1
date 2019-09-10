a_str = input("Input a string: ")
digit=[]

for i in a_str:
    if i.isdigit():
        digit.append(i)
print("".join(digit))