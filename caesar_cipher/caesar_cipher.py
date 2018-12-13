"""
Given a plaintext (string) and an encryption key (integer), my program should use the 'Caeser Cipher' method
to encrypt the plaintext. My program should not encrypt anything that isn't a character and should raise
an error if the encryption key goes above 25 or under 0.

Example: Given the string "One, 2, Three, Four, 5" with the encryption key 8, my program should return 'Wvm, 2, Bpzmm, Nwcz, 5'
"""

def caesar_cipher(plaintext, encrypt_key):
    if 25 < encrypt_key or encrypt_key < 0 :
        raise ValueError('Encryption Key must be between 0-25')
    ciphertext = list(plaintext)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            chip = ord(char) + encrypt_key
            if (char.lower() and chip > 122) or (char.istitle() and chip > 91):
                chip -= 26
            ciphertext[i] = chr(chip)
    return ''.join(ciphertext)
