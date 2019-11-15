random_words = ["lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"]
import random


def random_choice():
    random.seed(int(input("Random seed: ")))


def characters(word):
    print("The word you need to guess has "+str(len(word)),"characters")    ## hérna er ég að prenta út lengdina af orðinu í tölu
    return word


def guess(word, chars, counter=0):
    ord = ""                        ## búa til nýjann streng sem mun geyma stafina og fylla upp í með bandstrikum
    for ch in word:                ## búa til forloop sem skoðar hvern staf í orðinu sem var randomly valið
        if ch in chars:            ## og ef stafurinn er í chars listanum sem við bjuggum til áðann til þess að taka á móti stöfum sem er giskað á
            ord += ch + " "        ## þá tjekkum við hvort stafurinn sé í tóma strengnum og ef ekki þá bætum við honum við.
        else:
            ord += "- "             ## annars fyllum við uppí með bandstrikum.

    if word == ord.replace(" ",""):
        print("You won!")
        print("Word to guess:", ord)
        quit()
    if counter != 0:
        print("You are on guess ", str(counter) + "/12")
    print("Word to guess:", ord)
    return word


def checker(word):
    counter = 0
    chars = []

    while counter < 12:

        letter = input("Choose a letter: ")

        if letter not in chars:

            for ch in word:
                if ch == letter:
                    print("You guessed correctly!")
                    counter += 1
                    break
            else:
                print("The letter is not in the word!")

                counter += 1
            chars.append(letter)
        else:
            print("You have already guessed that letter!")
        guess(word, chars, counter)
    else:
        print("You lost! The secret word was ", word)





def main():
    random_choice()
    word = random.choice(random_words)
    characters(word)
    guess(word, [])
    checker(word)








main()