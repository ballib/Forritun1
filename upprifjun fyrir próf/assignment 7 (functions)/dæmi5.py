def is_palindrome(word):
    new_word = word.replace(",","").replace("!","").replace(" ","").replace(".","").lower()
    if new_word == new_word[::-1]:
        return True
    else:
        return False

def main():
    word = input("Enter a string: ")
    is_palindrome(word)
    if is_palindrome(word) == True:
        print("Is a palindrome")
    else:
        print("Is not a palindrome")

main()
