from word import data
import random
import string

#sagar
print(l1)

def rand_word():
    random_word=random.choice(data)
    while " "in random_word or "-" in random_word:
        random_word=random.choice(data)
    return random_word

def hangman():
    word=rand_word().upper()
    word_letter=set(word)
    alphabate=set(string.ascii_uppercase)
    used_letter = set()
    while(len(word_letter)>0):

        print("you have used this letters: "," ".join(used_letter))
        l=[letter if letter in used_letter else '-' for letter in word]
        s="".join(l)
        print(s)
        user_letter=input("enter letter ").upper()
        if user_letter in alphabate - used_letter:  #now alphabate has only those element which are not present in used_letter
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
        elif user_letter in used_letter:
            print("you have already used this letter, try agin")
        else:
            print("invalid input given")
    print(word)

hangman()
