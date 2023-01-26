import pandas as pd
import numpy as np

def make_guess(words):
    print("Submit your guess:")
    for i in reversed(range(4)):
        print("(You have "+str(i)+" tries remaining): ")
        attempt = str(input()).lower()
        if attempt in words:
            return attempt.lower()
        print("That wasn't a word in the word list. You have "+str(i)+" tries remaining\n")
    return -1


def get_information():
    allowed = "gywGYW"
    for i in reversed(range(4)):
        print("How correct was it?\n g = green, y = yellow, w = grey:")
        attempt = input()
        if len(attempt) == 5:
            if all(char in allowed for char in attempt):
                return attempt.lower()
        print("Not all inputs acceptable. You have "+str(i)+" tries remaining\n")
    return -1



def get_words(language):

    if language == 'german':
        print('Playing Wördle.de')
        fileloc = r'C:\Users\gregg\PycharmProjects\Wordle\word_banks\German_Word_Bank.txt'
        words = pd.read_csv(fileloc, sep=",", header=None, encoding="utf-8").to_numpy()[0]
    elif language == 'spanish':
        print(' Playing La Palabra Del Día')
        fileloc = r'C:\Users\gregg\PycharmProjects\Wordle\word_banks\Spanish_Word_Bank.txt'
        words = pd.read_csv(fileloc, sep=",", header=None, encoding="utf-8").to_numpy()[0]
    elif language == 'austrian':
        print('Playing wordle.at')
        fileloc = r'C:\Users\gregg\PycharmProjects\Wordle\word_banks\Austrian_Word_Bank.txt'
        words = pd.read_csv(fileloc, sep=',', header=None, encoding="utf-8").to_numpy()[0]
    else:
        print('Playing wordle (NYT Edition)')
        fileloc = r'C:\Users\gregg\PycharmProjects\Wordle\word_banks\English_Word_Bank.txt'
        words = pd.read_csv(fileloc, sep=",", header=None, encoding="utf-8").to_numpy()[0]

    #make all lowercase and make sure all words are strings!
    for i in range(len(words)):
        if type(words[i]) != str:
            words[i] = str(words[i])
        words[i] = words[i].lower()

    words = [word for word in words if len(word) == 5]
    for word in words:
        if len(word) != 5: # Just remove it...
            words = np.delete(words, i)

    return words

def determine_language():
    print("Available Languages are - English, German (AT, DE), and Spanish")
    print("Choose Your Character:")
    language = str(input()).lower()
    if 'at' in language:
        language = 'austrian'
    if 'de' in language:
        language = 'german'

    return language

