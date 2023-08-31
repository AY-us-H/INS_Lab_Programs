def monoalphabetic_substitution_cipher(plaintext, cipher_table):
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            if letter.isupper():
                ciphertext += cipher_table[letter]
            else:
                ciphertext += cipher_table[letter.upper()].lower()
        else:
            ciphertext += letter
    return ciphertext

def monoalphabetic_substitution_decryption(ciphertext, cipher_table):
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            if letter.isupper():
                plaintext += cipher_table.get(letter)
            else:
                plaintext += cipher_table.get(letter.upper(), letter).lower()
        else:
            plaintext += letter
    return plaintext

cipher_table = {
    "A": "Z",
    "B": "Y",
    "C": "X",
    "D": "W",
    "E": "V",
    "F": "U",
    "G": "T",
    "H": "S",
    "I": "R",
    "J": "Q",
    "K": "P",
    "L": "O",
    "M": "N",
    "N": "M",
    "O": "L",
    "P": "K",
    "Q": "J",
    "R": "I",
    "S": "H",
    "T": "G",
    "U": "F",
    "V": "E",
    "W": "D",
    "X": "C",
    "Y": "B",
    "Z": "A",
  
}

plaintext = input("Enter your text -> ")
print("Plaintext ->", plaintext)

ciphertext = monoalphabetic_substitution_cipher(plaintext, cipher_table)
print("Ciphertext ->", ciphertext)

decrypted_plaintext = monoalphabetic_substitution_decryption(ciphertext, cipher_table)
print("Decrypted plaintext ->", decrypted_plaintext)
