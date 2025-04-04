import re
keys_f = open('keys.txt', 'w')
possible_key = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz '
char_to_code = {char: idx for idx, char in enumerate(alphabet)}
code_to_char = {idx: char for idx, char in enumerate(alphabet)}
possible_keys = []
guess_keys = []
word_list = []
encoded1 = input("Adja meg az első rejtjelezett üzenetet: ").strip()
encoded2 = input("Adja meg a második rejtjelezett üzenetet: ").strip()
with open('words.txt', 'r') as f:
    for i in f:
        word_list.append(i.strip())
def decode_2(possible_key):
    if len(possible_key) >= len(encoded2):
        decoded_fragment = ''
        for i in range(min(len(possible_key), len(encoded2))):
            encoded_code = char_to_code[encoded2[i]]
            key_code = char_to_code[possible_key[i]]
            decoded_char_code = (encoded_code - key_code) % 27
            decoded_fragment += code_to_char[decoded_char_code]
        if all(word in word_list for word in decoded_fragment.split()):
            if len(possible_key) == len(encoded1):
                possible_keys.append(possible_key)
                return
            decode_1(possible_key)
    elif len(possible_key) >= len(encoded1):
        decoded_fragment = ''
        for i in range(min(len(possible_key), len(encoded2))):
            encoded_code = char_to_code[encoded2[i]]
            key_code = char_to_code[possible_key[i]]
            decoded_char_code = (encoded_code - key_code) % 27
            decoded_fragment += code_to_char[decoded_char_code]
        if decoded_fragment.split()[-1] == ' ':
            if all(word in word_list for word in decoded_fragment.split()):
                for word in word_list:
                    if len(word) <= len(encoded2) - len(decoded_fragment):
                        for i in range(len(word)):
                            encoded_code = char_to_code[encoded2[i + len(decoded_fragment)]]
                            word_code = char_to_code[word[i]]
                            key_char_code = (encoded_code - word_code) % 27
                            possible_key += code_to_char[key_char_code]
                        decode_1(possible_key)
            else:
                guesses = [word for word in word_list if word.startswith(decoded_fragment.split()[-1])]
                for guess in guesses:
                    if len(guess) <= len(encoded2) - len(" ".join(decoded_fragment.split()[0:-1]) + " "):
                        frag = ' '.join(map(str, decoded_fragment.split()[:-1])) + ' ' + guess + ' '
                        key_fragment = ''
                        for i in range(min(len(frag), len(encoded2))):
                            encoded_code = char_to_code[encoded2[i]]
                            frag_code = char_to_code[frag[i]]
                            key_char_code = (encoded_code - frag_code) % 27
                            key_fragment += code_to_char[key_char_code]
                        if key_fragment != possible_key:
                            decode_1(key_fragment)
        else:
            guesses = [word for word in word_list if word.startswith(decoded_fragment.split()[-1])]
            for guess in guesses:
                if len(guess) <= len(encoded2) - len(" ".join(decoded_fragment.split()[0:-1]) + " "):
                    frag = ' '.join(map(str, decoded_fragment.split()[:-1])) + ' ' + guess + ' '
                    key_fragment = ''
                    for i in range(min(len(frag), len(encoded2))):
                        encoded_code = char_to_code[encoded2[i]]
                        frag_code = char_to_code[frag[i]]
                        key_char_code = (encoded_code - frag_code) % 27
                        key_fragment += code_to_char[key_char_code]
                    if key_fragment != possible_key:
                        decode_1(key_fragment)
    else:
        decoded_fragment = ''
        for i in range(min(len(possible_key), len(encoded2))):
            encoded_code = char_to_code[encoded2[i]]
            key_code = char_to_code[possible_key[i]]
            decoded_char_code = (encoded_code - key_code) % 27
            decoded_fragment += code_to_char[decoded_char_code]
        if all(word in word_list for word in decoded_fragment.split()):
            if len(possible_key) == max(len(encoded1), len(encoded2)):
                possible_keys.append(possible_key)
                return
        if all(word in word_list for word in decoded_fragment.split()[0:-1]):
            guesses = [word for word in word_list if word.startswith(decoded_fragment.split()[-1])]
            for guess in guesses:
                if len(guess) <= len(encoded2) - len(" ".join(decoded_fragment.split()[0:-1]) + " "):
                    frag = ' '.join(map(str, decoded_fragment.split()[:-1])) + ' ' + guess + ' '
                    key_fragment = ''
                    for i in range(min(len(frag), len(encoded2))):
                        encoded_code = char_to_code[encoded2[i]]
                        frag_code = char_to_code[frag[i]]
                        key_char_code = (encoded_code - frag_code) % 27
                        key_fragment += code_to_char[key_char_code]
                    if key_fragment != possible_key:
                        decode_1(key_fragment)

def decode_1(possible_key):
    if len(possible_key) >= len(encoded1):
        decoded_fragment = ''
        for i in range(min(len(possible_key), len(encoded1))):
            encoded_code = char_to_code[encoded1[i]]
            key_code = char_to_code[possible_key[i]]
            decoded_char_code = (encoded_code - key_code) % 27
            decoded_fragment += code_to_char[decoded_char_code]
        if all(word in word_list for word in decoded_fragment.split()):
            if len(possible_key) == len(encoded2):
                possible_keys.append(possible_key)
                return
            decode_2(possible_key)
    elif len(possible_key) >= len(encoded2):
        decoded_fragment = ''
        for i in range(min(len(possible_key), len(encoded1))):
            encoded_code = char_to_code[encoded1[i]]
            key_code = char_to_code[possible_key[i]]
            decoded_char_code = (encoded_code - key_code) % 27
            decoded_fragment += code_to_char[decoded_char_code]
        if decoded_fragment.split()[-1] == ' ':
            if all(word in word_list for word in decoded_fragment.split()):
                for word in word_list:
                    if len(word) <= len(encoded1) - len(decoded_fragment):
                        for i in range(len(word)):
                            encoded_code = char_to_code[encoded1[i + len(decoded_fragment)]]
                            word_code = char_to_code[word[i]]
                            key_char_code = (encoded_code - word_code) % 27
                            possible_key += code_to_char[key_char_code]
                        decode_2(possible_key)
            else:
                guesses = [word for word in word_list if word.startswith(decoded_fragment.split()[-1])]
                for guess in guesses:
                    if len(guess) <= len(encoded1) - len(" ".join(decoded_fragment.split()[0:-1]) + " "):
                        frag = ' '.join(map(str, decoded_fragment.split()[:-1])) + ' ' + guess + ' '
                        key_fragment = ''
                        for i in range(min(len(frag), len(encoded1))):
                            encoded_code = char_to_code[encoded1[i]]
                            frag_code = char_to_code[frag[i]]
                            key_char_code = (encoded_code - frag_code) % 27
                            key_fragment += code_to_char[key_char_code]
                        if key_fragment != possible_key:
                            decode_2(key_fragment)
        else:
            guesses = [word for word in word_list if word.startswith(decoded_fragment.split()[-1])]
            for guess in guesses:
                if len(guess) <= len(encoded1) - len(" ".join(decoded_fragment.split()[0:-1]) + " "):
                    frag = ' '.join(map(str, decoded_fragment.split()[:-1])) + ' ' + guess + ' '
                    key_fragment = ''
                    for i in range(min(len(frag), len(encoded1))):
                        encoded_code = char_to_code[encoded1[i]]
                        frag_code = char_to_code[frag[i]]
                        key_char_code = (encoded_code - frag_code) % 27
                        key_fragment += code_to_char[key_char_code]
                    if key_fragment != possible_key:
                        decode_2(key_fragment)
    else:
        decoded_fragment = ''
        for i in range(min(len(possible_key), len(encoded1))):
            encoded_code = char_to_code[encoded1[i]]
            key_code = char_to_code[possible_key[i]]
            decoded_char_code = (encoded_code - key_code) % 27
            decoded_fragment += code_to_char[decoded_char_code]
        if all(word in word_list for word in decoded_fragment.split()):
            if len(possible_key) == max(len(encoded1), len(encoded2)):
                possible_keys.append(possible_key)
                return
        if all(word in word_list for word in decoded_fragment.split()[0:-1]):
            guesses = [word for word in word_list if word.startswith(decoded_fragment.split()[-1])]
            for guess in guesses:
                if len(guess) <= len(encoded1) - len(" ".join(decoded_fragment.split()[0:-1]) + " "):
                    frag = ' '.join(map(str, decoded_fragment.split()[:-1])) + ' ' + guess + ' '
                    key_fragment = ''
                    for i in range(min(len(frag), len(encoded1))):
                        encoded_code = char_to_code[encoded1[i]]
                        frag_code = char_to_code[frag[i]]
                        key_char_code = (encoded_code - frag_code) % 27
                        key_fragment += code_to_char[key_char_code]
                    if key_fragment != possible_key:
                        decode_2(key_fragment)

for word in word_list:
    if len(word) <= len(encoded1):
        possible_key = ''
        for i in range(len(word)):
            encoded_code = char_to_code[encoded1[i]]
            word_code = char_to_code[word[i]]
            key_char_code = (encoded_code - word_code) % 27
            possible_key += code_to_char[key_char_code]
        decode_2(possible_key)

valid_keys = [key for key in possible_keys if len(key) == max(len(encoded1), len(encoded2))]
if valid_keys:
    unique_keys = []
    [unique_keys.append(key) for key in valid_keys if key not in unique_keys]
    keys_f.write(f"{'\n'.join(unique_keys)}")
    print(f"The keys have been written to keys.txt ({len(unique_keys)})")
else:
    print("No keys found.")
keys_f.close()


def decode_message(encoded_message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    char_to_code = {char: idx for idx, char in enumerate(alphabet)}
    code_to_char = {idx: char for idx, char in enumerate(alphabet)}

    decoded_message = ''
    for i in range(len(encoded_message)):
        encoded_code = char_to_code[encoded_message[i]]
        key_code = char_to_code[key[i]]
        decoded_char = (encoded_code - key_code) % 27
        decoded_message += code_to_char[decoded_char]

    return decoded_message
m = open("message.txt", "w")
with open("keys.txt", "r") as f:
    for line in f:
        key = line.strip("\n")
        m.write(f"Key: {key}\n")
        decoded_message1 = decode_message(encoded1, key)
        decoded_message2 = decode_message(encoded2, key)
        m.write(f"Decoded message1: {decoded_message1}\n")
        m.write(f"Decoded message2: {decoded_message2}\n")
        m.write("\n")
print("The decoded messages have been written to message.txt")
m.close()