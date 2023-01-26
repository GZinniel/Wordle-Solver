HARDCORE = True
ATTEMPTS = 10

import word_elimination as we
if HARDCORE:
    import HARDCORE_word_guessing as odds
else:
    import word_guessing as odds
from guessing import *

language = determine_language()
possible_words = get_words(language)
all_words = possible_words


for tries in range(ATTEMPTS):
    print("Attempt "+str(tries+1)+"/6 - Here are some optimal guesses (" + str(len(possible_words)) + " Options Remaining):")

    best_guesses, worst_guesses = odds.find_best_guesses(all_words, possible_words)
    print(best_guesses)
    print(worst_guesses)

    guess = make_guess(all_words)
    if guess == -1:
        break

    information = get_information()
    if information == -1:
        break

    if information == 'ggggg':
        print("Congrats! You Did it")
        break

    possible_words = we.word_cull(guess, information, possible_words)

print("Thanks for Playing!")
