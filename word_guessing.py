import pandas as pd

def count_char_score_plur(i, char, words):
    w_score, g_score, y_score = 0, 0, 0

    # Filter though all the words
    for word in words:

        # if the character is in the word, then it
        if char in word:
            w_score = w_score + 1

        selected_y, selected_g = False, False
        for pos in i:
            if word[pos] == char: selected_g = True
            if word[pos] != char and char in word: selected_y = True

        if selected_g == True: g_score = g_score + 1
        if selected_y: y_score = y_score + 1

    return w_score, g_score, y_score

def char_score_plur(pos, char, words):
    w_elim, g_elim, y_elim = count_char_score_plur(pos, char, words)
    tot = len(words)

    w_score = w_elim * (tot - w_elim)
    g_score = g_elim * (tot - g_elim)
    y_score = y_elim * (tot - y_elim)

    tot_score = 2 * (w_score + g_score + y_score) / (3 * tot)

    return tot_score


def count_char_score_sig(pos, char, words):
    w_score, g_score, y_score = 0, 0, 0

    # Filter though all the words
    for word in words:
        # if the character is in the word, then it
        if char in word:                       w_score = w_score + 1
        if word[pos] == char:                  g_score = g_score + 1
        if word[pos] != char and char in word: y_score = y_score + 1
    return w_score, g_score, y_score

def char_score_sig(pos, char, words):
    w_elim, g_elim, y_elim = count_char_score_sig(pos, char, words)
    tot = len(words)

    w_score = w_elim * (tot - w_elim)
    g_score = g_elim * (tot - g_elim)
    y_score = y_elim * (tot - y_elim)

    tot_score = 2 * (w_score + g_score + y_score) / (3 * tot)

    return tot_score

def find_duplicates (word):
    result = {}
    for pos, char in enumerate(word):
        if char in result.keys():
            temp = result[char]
            temp.append(pos)
            result[char] = temp
        else:
            result[char] = [pos]
    return result

def parce_word_list(words):
    # Find all letter posiitons left
    result = {}
    for word in words:
        for pos, char in enumerate(word):
            if char in result.keys():
                if pos not in result[char]:
                    temp = result[char]
                    temp.append(pos)
                    result[char] = temp
            else:
                result[char] = [pos]
    for letter in result:
        temp = result[letter]
        temp.sort()
        result[letter] = temp

    # Score each Letter position singularly
    score = []
    for letter in result:
        score = []
        for position in result[letter]:
            score.append(char_score_sig(position, letter, words))
        result[letter] = score

    return result

def average_score(points, length):
    total_score = 1
    for pos, score in enumerate(points):
        # points[pos] = 1 - (score / length)
        total_score = total_score * (1 - (score / length))

    total_score = length - total_score * length

    return total_score


def find_best_guesses(_, words):
    # All Letter Scores
    letter_scores = parce_word_list(words)

    # Now we make the word_dict
    word_dict = {}

    for word in words:
        word_dict[word] = find_duplicates(word)

    for word in word_dict:
        points = []
        for char in word_dict[word]:
            if len(word_dict[word][char]) == 1:

                try:
                    points.append(letter_scores[char][word_dict[word][char][0]])
                except IndexError:
                    points.append(letter_scores[char][0])
                    print("Wow what happened! word_guessing:127")

            else:
                points.append(char_score_plur(word_dict[word][char], char, words))
        word_dict[word] = average_score(points, len(words))

    optimal_guesses = {}

    if len(word_dict) > 6:
        for i in range(6):
            best_guess = max(word_dict, key=word_dict.get)
            optimal_guesses[best_guess] = round(word_dict[best_guess])
            del word_dict[best_guess]
    else:
        for guess in word_dict:
            optimal_guesses[guess] = round(word_dict[guess])

    """
    if len(word_dict) > 3:
        for i in range(3):
            worst_guess = min(word_dict, key=word_dict.get)
            optimal_guesses[worst_guess] = round(word_dict[worst_guess])
            del word_dict[worst_guess]
    else:
        for guess in word_dict:
            optimal_guesses[guess] = round(word_dict[guess])
    """

    return optimal_guesses
