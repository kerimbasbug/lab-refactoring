import random

from pyfiglet import Figlet
from pyfiglet import print_figlet

key_words_list = ['Encryption', 'Database', 'Algorithm',
                  'Cryptology', 'Python', 'Ironhack']  # list of words and the alphabet
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

tried_letters_set = set()  # set of letters entered as input
guess_of_user_list = []

index = random.randint(0, len(key_words_list) - 1)  # random integer for the index
key_word = key_words_list[index]  # our key word
key_word_as_list = []

# converting the key_word to a list called key_word_as_list
for i in range(len(key_word)):
    key_word_as_list.append(key_word[i].upper())


# prints the word in the console
def print_updated_str(user__input_ch):
    for i in range(len(key_word_as_list)):
        if key_word_as_list[i] == user__input_ch:
            guess_of_user_list[i] = user__input_ch

str_to_print = ""
    
    for i in range(len(guess_of_user_list)):
        str_to_print = str_to_print + guess_of_user_list[i] + " "
    
    custom_fig = Figlet(font='standard')
    print(custom_fig.renderText(str_to_print))


# function to print the hangman
def print_hangman(fault):
    if fault == 1:
        print("""
            |
            |
            |
            |
            |
            _|_
            """)
    elif fault == 2:
        print("""
            ________
            |
            |
            |
            |
            |
            _|_
            """)
    elif fault == 3:
        print("""
            ________
            |        |
            |
            |
            |
            |
            _|_
            """)
    elif fault == 4:
        print("""
            ________
            |        |
            |        O
            |
            |
            |
            _|_
            """)
    elif fault == 5:
        print("""
            ________
            |        |
            |        O
            |        |
            |        |
            |
            _|_
            """)
    elif fault == 6:
        print("""
            ________
            |        |
            |        O
            |       /|\
            |        |
            |
            _|_
            """)
    else:
        print("""
            ________
            |        |
            |        O
            |       /|\
            |        |
            |       / \
            _|_
            """)
        colors = "31;31;31"
        print_figlet("YOU ARE DEAD", font="standard", colors=colors)
        exit()


# driver function for the game
def play():
    colors = "31;31;31"
    print_figlet("Welcome To", font="standard", colors=colors)
    print_figlet("H A N G M A N", font="standard", colors=colors)
    
    user_fault = 0
    max_fault = 7
    
    space = "_ " * len(key_word_as_list)
    custom_fig = Figlet(font='standard')
    print(custom_fig.renderText(space))
    
    for i in range(len(key_word_as_list)):
        guess_of_user_list.append("_")

    while (user_fault < max_fault):
        if (guess_of_user_list == key_word_as_list):
            colors = "31;31;31"
            print_figlet("! ! !CONGRATS! ! !", font="standard", colors=colors)
            break
        else:
            user__input_ch = str(input("Enter a letter: "))
            while user__input_ch not in alphabet:
                user__input_ch = str(input("Please enter a letter: "))
            
            if user__input_ch in tried_letters_set:
                print("You have already used letter(s)", tried_letters_set)
                user__input_ch = str(input("Please enter a new letter: "))
            else:
                tried_letters_set.add(user__input_ch)
            
            if user__input_ch in key_word_as_list:
                print_updated_str(user__input_ch)
            
            else:
                user_fault = user_fault + 1
                print_hangman(user_fault)
return


play()
