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

# Példa használat:
message = "helloworld"
key = "abcdefgijkl"
encoded_message = encode_message(message, key)
print("Encoded:", encoded_message)  # "hfnosauzun"

decoded_message = decode_message(encoded_message, key)
print("Decoded:", decoded_message)  # "helloworld"