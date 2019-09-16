# find_min function definition goes here
def find_min():
    if first > second:
        return second
    else:
        return first

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

# Call the function here
print("Minimum: ", find_min())