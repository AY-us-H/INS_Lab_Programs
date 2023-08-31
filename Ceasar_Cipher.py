def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage
plaintext = input("Enter your text -> ")
key = int(input("Enter key value -> "))
encrypted_text = caesar_encrypt(plaintext, key)
decrypted_text = caesar_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
