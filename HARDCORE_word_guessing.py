def count_char_score_plur(i, char, possible_words):
    w_score, g_score, y_score = 0, 0, 0

    # Filter though all the words
    for word in possible_words:

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


def char_score_plur(pos, char, possible_words):
    w_elim, g_elim, y_elim = count_char_score_plur(pos, char, possible_words)
    tot = len(possible_words)

    w_score = w_elim * (tot - w_elim)
    g_score = g_elim * (tot - g_elim)
    y_score = y_elim * (tot - y_elim)

    tot_score = 2 * (w_score + g_score + y_score) / (3 * tot)

    return tot_score


def count_char_score_sig(pos, char, possible_words):
    w_score, g_score, y_score = 0, 0, 0

    # Filter though all the words
    for word in possible_words:
        # if the character is in the word, then it
        if char in word:                       w_score = w_score + 1
        if word[pos] == char:                  g_score = g_score + 1
        if word[pos] != char and char in word: y_score = y_score + 1
    return w_score, g_score, y_score


def char_score_sig(pos, char, possible_words):
    w_elim, g_elim, y_elim = count_char_score_sig(pos, char, possible_words)
    tot = len(possible_words)

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


def parce_word_list(all_words, possible_words):

    for word in all_words:
        try:
            for pos, char in enumerate(word):
                happy = char
        except TypeError:
            x = 7
            print(word)
            z = 8




    # Find all letter positions left
    result = {}
    for word in all_words:
        for pos, char in enumerate(word):
            if char in result.keys():
                if pos not in result[char]:
                    temp = result[char]
                    temp.append(pos)
                    result[char] = temp
            else:
                result[char] = [pos]

    # Sort the letters A -> Z
    for letter in result:
        temp = result[letter]
        temp.sort()
        result[letter] = temp

    # Score each Letter position singularly
    for letter in result:
        score = []
        for position in result[letter]:
            score.append(char_score_sig(position, letter, possible_words))
        result[letter] = score

    return result


def average_score(points, length):
    total_score = 1
    for score in points:
        total_score = total_score * (1 - (score / length))

    total_score = length - total_score * length

    return total_score


def get_optimal_guesses(word_dict, BEST=6, WORST=0, round_to_int = True):
    supplied_guesses = {}

    # Get a prescribed number of best guesses
    supplied_guesses['BEST'] = ':)'
    while len(supplied_guesses) < BEST + 1:
        # If no options left, can't add any more guesses
        if len(word_dict) == 0:
            break

        # Pull the best guess
        best_guess = max(word_dict, key=word_dict.get)

        # Only add to DICT if it isn't 0 (pointless if it is 0)
        if word_dict[best_guess] > 0:
            supplied_guesses[best_guess] = word_dict[best_guess]
        del word_dict[best_guess]

    # Get a prescribed number of worst guesses as well (just for fun)
    worst_guess_list = []
    if WORST > 0:
        supplied_guesses['WORST'] = ':('
    while len(worst_guess_list) < WORST:
        # If no options left, can't add any more guesses
        if len(word_dict) == 0:
            break

        # Pull the worst guess left
        worst_guess = min(word_dict, key=word_dict.get)

        # Only add to DICT if it isn't 0 (pointless if it is 0)
        if word_dict[worst_guess] > 0:
            worst_guess_list.append((worst_guess, word_dict[worst_guess]))
        del word_dict[worst_guess]

    # Now add all the worst guesses into DICT
        for guesses in reversed(worst_guess_list):
            supplied_guesses[guesses[0]] = guesses[1]

    # Afterwards, we round them to a whole number, so it is easier to read
    if round_to_int:
        for guess in supplied_guesses:
            if type(supplied_guesses[guess]) == float:
                supplied_guesses[guess] = round(supplied_guesses[guess])

    return supplied_guesses


def find_best_guesses(all_words, possible_words):
    # All Letter Scores
    letter_scores = parce_word_list(all_words, possible_words)

    # Now we make the word_dict
    word_dict = {}

    for word in all_words:
        word_dict[word] = find_duplicates(word)

    for word in word_dict:
        points = []
        for char in word_dict[word]:
            if len(word_dict[word][char]) == 1:

                try:
                    points.append(letter_scores[char][word_dict[word][char][0]])
                except IndexError:
                    points.append(letter_scores[char][0])

            else:
                points.append(char_score_plur(word_dict[word][char], char, possible_words))
        word_dict[word] = average_score(points, len(possible_words))

    # Now weigh in possibility of being correct
    for word in word_dict:
        if word in possible_words:
            if word_dict[word] == 0:
                word_dict[word] += 1
            else:
                word_dict[word] = word_dict[word] * (1 + 1/len(possible_words))

    #Print out all remaining word options as well as their "score"
    """
    others = {}
    for word in possible_words:
        others[word] = round(word_dict[word])
    print(others)
    """

    optimal_guesses = get_optimal_guesses(word_dict, BEST=3, WORST=3)

    return optimal_guesses

