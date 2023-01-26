def find_duplicates(guess):
    result = {}
    for char in set(guess):
        result[char] = guess.count(char)
    return result


def regular_removal(words, guess, information, indices, letter):
    # For letters not in word
    for i in indices:
        if information[i] == 'w':
            words = remove_w(guess[i], words)

    # For letters in correct spot
    for i in indices:
        if information[i] == 'g':
            words = remove_g(i, guess[i], words)

    # For letters in word, but not the right spot
    for i in indices:
        if information[i] == 'y':
            words = remove_y(i, guess[i], words)

    return words


def remove_w(incorrect, words):

    words = list(filter(lambda word: incorrect not in word, words))
    """
    for word in words:
        if incorrect in word:
            words.remove(word)
    """
    return words


def remove_g(i, correct, words):

    words = list(filter(lambda word: correct == word[i], words))

    """
    for word in words:
        if word[i] != correct:
            words.remove(word)
    """

    return words


def remove_y(i, correct, words):

    words = list(filter(lambda word: correct!=word[i] and correct in word, words))

    """
    for word in words:
        if correct not in word or word[i] == correct:
            words.remove(word)
    """

    return words


def remove_duplicate_letters(letter, amount, words):

    words = list(filter(lambda word: amount > word.count(letter), words))

    """
    for word in words:
        if word.count(letter) > amount:
            words.remove(word)
    """

    return words


def word_cull(guess, information, words):
    occurrences = find_duplicates(guess)

    for letter in occurrences:
        indices = [i for i in range(len(guess)) if guess.startswith(letter, i)]

        if occurrences[letter] == 1:
            words = regular_removal(words, guess, information, indices, letter)

        else: # occurences[letter] >= 2:
            for i in indices:
                findcase = [information[i] for i in indices]

            if findcase.count('w') > 0:
                words = remove_duplicate_letters(letter, len(findcase) - findcase.count('w'), words)

            for i, info in list(enumerate(findcase)):
                if info == 'g':
                    words = remove_g(indices[i], letter, words)
                if info == 'y':
                    words, remove_y(indices[i], letter, words)

    print("\n\n\n")
    print(words)
    print("\n\n\n")

    return words
