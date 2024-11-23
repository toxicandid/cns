import random


def generate_key(plaintext_length):
    key = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(plaintext_length))
    return key


def value_of_string(text):
    result = [(ord(char) - ord('a')) for char in text]
    return result


def vernam_encrypt(plaintext, key):
    encrypted_text = ''
    cipher_values = []
    value_of_plaintext = value_of_string(plaintext)
    value_of_key = value_of_string(key)
    print(value_of_plaintext, value_of_key)

    for i in range(0, len(value_of_plaintext)):
        cipher_value = value_of_plaintext[i] ^ value_of_key[i]

        cipher_values.append(cipher_value)
        encrypted_text += chr(cipher_value + ord('a'))

    return encrypted_text


def vernam_decrypt(encrypted_text, key):
    decrypted_text = ''
    plain_values = []
    value_of_encrypted = value_of_string(encrypted_text)
    value_of_key = value_of_string(key)
    print(value_of_encrypted, value_of_key)

    for i in range(0, len(value_of_encrypted)):
        plain_value = value_of_encrypted[i] ^ value_of_key[i]

        plain_values.append(plain_value)
        decrypted_text += chr(plain_value + ord('a'))

    return decrypted_text


def main():
    plaintext = "helloiamaiiwillconqujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjerworldhehehe"
    key = generate_key(len(plaintext))
    encrypted_text = vernam_encrypt(plaintext, key)
    decrypted_text = vernam_decrypt(encrypted_text, key)
    print(encrypted_text, decrypted_text)


if __name__ == "__main__":
    main()