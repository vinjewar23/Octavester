import sys

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')
            new_char = chr((ord(char) - shift + key_shift) % 26 + shift)
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')
            new_char = chr((ord(char) - shift - key_shift) % 26 + shift)
            plaintext += new_char
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter the text: ")
    key = input("Enter the key: ")

    print("\nOptions:")
    print("1. Encrypt")
    print("2. Decrypt")

    option = int(input("\nEnter your option: "))
    if(option == 1):
        ciphertext = vigenere_encrypt(plaintext, key)
        print("Encrypted message:", ciphertext)
    elif(option == 2):
        decrypted_text = vigenere_decrypt(plaintext, key)
        print("Decrypted message:", decrypted_text)
    else:
        print("Invalid option")
    
    input("\n\033[33mPress Enter to return to Main menu\n\n\033[0m")
    sys.exit()

 


    

    