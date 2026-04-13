"""Module providing the Caesar Cipher."""

def rotate(text, key):
    """Return text encrypted with a Caesar cipher using the given key."""
    cipher = []
    for letter in text:
        if letter.isalpha():
            base = ord('a') if letter.islower() else ord('A')
            cipher.append(chr((ord(letter) - base + key) % 26 + base))
        else:
            cipher.append(letter)
    
    return ''.join(cipher)