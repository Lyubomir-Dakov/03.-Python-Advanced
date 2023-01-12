from collections import deque


def word_found(words):
    for x in words.values():
        if len(x) == 0:
            return True
    return False


vowels = deque(x for x in input().split())
consonants = [x for x in input().split()]

special_words = {
    'rose': 'rose',
    'tulip': 'tulip',
    'lotus': 'lotus',
    'daffodil': 'daffodil'
}

while True:
    if not vowels or not consonants or word_found(special_words):
        break

    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word in special_words:
        current_word = [x for x in special_words[word]]
        if current_vowel in current_word:
            while current_vowel in current_word:
                current_word.remove(current_vowel)
        if current_consonant in current_word:
            while current_consonant in current_word:
                current_word.remove(current_consonant)
        special_words[word] = ''.join(current_word)

word_is_found = False

for word, value in special_words.items():
    if len(value) == 0:
        print(f"Word found: {word}")
        word_is_found = True
        break

if not word_is_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
