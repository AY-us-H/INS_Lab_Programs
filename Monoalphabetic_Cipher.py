def monoalphabetic_substitution_cipher(plaintext, cipher_table):
  ciphertext = ""
  for letter in plaintext:
    letter = letter.lower()
    ciphertext += cipher_table.get(letter, letter)
  return ciphertext

def monoalphabetic_substitution_decryption(ciphertext, cipher_table):
  plaintext = ""
  for letter in ciphertext:
    letter = letter.lower()
    plaintext += cipher_table.get(letter, letter)
  return plaintext

cipher_table = {
    "a": "z",
    "b": "y",
    "c": "x",
    "d": "w",
    "e": "v",
    "f": "u",
    "g": "t",
    "h": "s",
    "i": "r",
    "j": "q",
    "k": "p",
    "l": "o",
    "m": "n",
    "n": "m",
    "o": "l",
    "p": "k",
    "q": "j",
    "r": "i",
    "s": "h",
    "t": "g",
    "u": "f",
    "v": "e",
    "w": "d",
    "x": "c",
    "y": "b",
    "z": "a"
  }

plaintext = input("Enter your text -> ")
ciphertext = monoalphabetic_substitution_cipher(plaintext, cipher_table)
print("Ciphertext:", ciphertext)

decrypted_plaintext = monoalphabetic_substitution_decryption(ciphertext, cipher_table)
print("Decrypted plaintext:", decrypted_plaintext)
