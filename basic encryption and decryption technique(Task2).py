"""This is a python program which encrypts and decrypts text using ceaser cipher technique."""
def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char

    return decrypted_text


message = input("Enter text: ")
shift = int(input("Enter shift key: "))

encrypted_msg= encrypt(message, shift)
decrypted_msg = decrypt(encrypted_msg, shift)

print("\nEncrypted Text:", encrypted_msg)
print("Decrypted Text:", decrypted_msg)