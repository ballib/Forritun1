# Your function definition goes here
def count_case(user_input):
    upper = 0
    lower = 0
    for ch in user_input:
        if ch.isupper():
            upper += 1
        else:
            lower +=1
    return upper, lower
user_input = input("Enter a string: ")

# Call the function here
upper, lower = count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)