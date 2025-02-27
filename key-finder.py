import re

def load_word_list(file_path):
    with open(file_path, 'r') as f:
        words = f.read().splitlines()
    return words

def find_keys(encoded1, encoded2, word_list):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    char_to_code = {char: idx for idx, char in enumerate(alphabet)}
    code_to_char = {idx: char for idx, char in enumerate(alphabet)}

    possible_keys = []

    for word in word_list:
        if len(word) > len(encoded1):
            continue

        possible_key = ''
        for i in range(len(word)):
            encoded_code = char_to_code[encoded1[i]]
            word_code = char_to_code[word[i]]
            key_char_code = (encoded_code - word_code) % 27
            possible_key += code_to_char[key_char_code]

        decoded2_fragment = ''
        for i in range(len(possible_key)):
            encoded_code = char_to_code[encoded2[i]]
            key_code = char_to_code[possible_key[i]]
            decoded_char = (encoded_code - key_code) % 27
            decoded2_fragment += code_to_char[decoded_char]

        if any(decoded2_fragment.startswith(word[:i+1]) for i in range(len(word))):
            possible_keys.append(possible_key)

    return possible_keys

encoded1 = input("Adja meg az első rejtjelezett üzenetet: ").strip()
encoded2 = input("Adja meg a második rejtjelezett üzenetet: ").strip()

word_list = load_word_list('words.txt')

possible_keys = find_keys(encoded1, encoded2, word_list)
if possible_keys:
    print("Lehetséges kulcsok:", possible_keys)
else:
    print("Nem található lehetséges kulcs.")