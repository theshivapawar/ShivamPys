texts = ['abc', 'aba', 'lol', 'cli']
palindrome_texts = list(filter(lambda s : s == s[::-1], texts))
print(palindrome_texts)

numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10]
odd_squares = list(map(lambda n : n ** 2, filter(lambda n : n % 2 != 0, numbers)))
print(odd_squares)

words = ['abc', 'hello', 'car', 'hehe']

# def has_duplicate_char(word):
#     uniques = []
#     for char in word:
#         if char in uniques:
#             return True
#         uniques.append(char)
#     return False

def has_duplicate_char(word):
    for char in word:
        if word.count(char) > 1:
            return True
    return False

duplicate_char_words = list(filter(has_duplicate_char, words))
print(duplicate_char_words)

titles = ['hey', 'Mey', 'key Ley', 'Zey']
swapped = list(map(lambda s : s.swapcase() if s[0].islower() else s, titles))
print(swapped)

