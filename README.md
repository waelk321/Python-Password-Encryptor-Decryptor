# Python-Password-Encryptor-Decryptor
Simple Python program to encrypt/decrypt passwords using a shuffled character mapping
Supports letters, digits, punctuation, and spaces

This project uses two lists:

encrypt: the original alphabet (space + punctuation + letters + digits)

key: a shuffled copy of that alphabet

Encryption maps each character from encrypt → key by index.
Decryption reverses the mapping from key → encrypt.
