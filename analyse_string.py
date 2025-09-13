def analyse_text(text):
    words = text.split(' ')
    number_of_words = len(words)

    uniques = []

    for word in words:
        if word not in uniques:
            new_word = []
            for char in word:
                if char.isalpha():
                    new_word.append(char)
            uniques.append(''.join(new_word).lower())

    number_of_uniques = len(uniques)

    number_of_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in words:
        for char in word:
            if char.lower() in vowels:
                number_of_vowels += 1

    longest_word = ''
    for word in uniques:
        if len(word) > len(longest_word):
            longest_word = word

    length_count = {}
    for word in words:
        if len(word) not in length_count:
            length_words = []
            length_words.append(word)
            length_count[len(word)] = length_words
        else:
            length_count[len(word)].append(word)

    common_length_words = []
    for value in length_count.values():
        if len(value) > len(common_length_words):
            common_length_words = value

    return number_of_words, number_of_uniques, number_of_vowels, longest_word, common_length_words


print(analyse_text('Hello How are you What are you doing'))
