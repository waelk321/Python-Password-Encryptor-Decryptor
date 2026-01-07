import random
import string 

def encrypt_password(password):
    global encrypt
    encrypt = " " + string.punctuation+string.ascii_letters + string.digits
    encrypt = list(encrypt)
    global key
    key = encrypt.copy()
    random.shuffle(key)
    newpassword = " "
    for letter in password:
        index = encrypt.index(letter)
        newpassword += key[index]
    return newpassword

def decrypt_password(password):
    originalpassword = ""
    for letter in password:
        if letter not in key:
            originalpassword += letter
            continue
        index = key.index(letter)
        originalpassword += encrypt[index]
    return originalpassword

print("Welcome to the Password Encryptor!")
print("-----------------------------------")
choice = 0
while (choice != 3):
    print("What do you wish to do ?")
    print("1. Encrypt a password")
    print("2. Decrypt a password")
    print("3. Exit")
    choice = int(input("Enter 1, 2 or 3: "))
    if choice > 3 or choice < 1:
        print("Invalid choice, please try again.")
    if choice == 1:
        print("enter your password to encrypt:")
        input_password = input()
        print("You entered: " + input_password)
        print (f"Your encrypted password is:{encrypt_password(input_password)}")
    elif choice == 2:
        print("enter your password to decrypt:")
        input_password = input()
        print (f"Your decrypted password is: {decrypt_password(input_password)}")
    elif choice == 3:
        print("Exiting the program. Goodbye!")
       
    input("Press Enter to continue...")