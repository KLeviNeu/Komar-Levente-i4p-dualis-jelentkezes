import re

def validate_input(message, key):
    if not re.fullmatch(r"[a-z ]+", message):
        raise ValueError("Az üzenet csak az angol ábécé kisbetűit és szóközt tartalmazhat!")
    if not re.fullmatch(r"[a-z ]+", key):
        raise ValueError("A kulcs csak az angol ábécé kisbetűit és szóközt tartalmazhat!")
    
    if len(key) < len(message):
        raise ValueError("A kulcsnak legalább akkorának kell lennie, mint az üzenet!")

def encode_message(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    char_to_code = {char: idx for idx, char in enumerate(alphabet)}
    code_to_char = {idx: char for idx, char in enumerate(alphabet)}

    encoded_message = ''
    for i in range(len(message)):
        message_code = char_to_code[message[i]]
        key_code = char_to_code[key[i]]
        encoded_char = (message_code + key_code) % 27
        encoded_message += code_to_char[encoded_char]

    return encoded_message

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

message = input("Adja meg az üzenetet: ").strip()
key = input("Adja meg a kulcsot: ").strip()

try:
    validate_input(message, key)
except ValueError as e:
    print(f"Hiba: {e}")

encoded_message = encode_message(message, key)
print("Rejtjelezett üzenet:", encoded_message)

decoded_message = decode_message(encoded_message, key)
print("Visszafejtett üzenet:", decoded_message)