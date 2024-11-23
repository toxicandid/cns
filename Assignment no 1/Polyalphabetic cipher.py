def value_of_key(key):
    return [ord(char.lower()) - ord('a') for char in key]

def encrypt(plaintext, key):
    shifts = value_of_key(key)
    result = []
    key_length = len(shifts)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = shifts[i%key_length]
            new_char = chr((ord(char) - base + shift)%26 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def decrypt(plaintext, key):
    shifts = value_of_key(key)
    result = []
    key_length = len(shifts)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = shifts[i % key_length]
            new_char = chr((ord(char) - base - shift)%26 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

plaintext = "i amaixY 9 z"
key = "dobby"

encrypted_text = encrypt(plaintext, key)
decrypted_text = decrypt(encrypted_text, key)

print(f"Encrypted: {encrypted_text} ------- Decrypted: {decrypted_text}")

'''
TC = O(n) both encryption and decryption
Adv:
    - resists frequency analysis because multiple letters map to each plaintext letter
    - long key --> increased strength

'''
