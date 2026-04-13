"""Module providing a function implementing the Caesar Cipher."""

def rotate(text, key):
    cypher = []
    for letter in text:
        if letter.isalpha():
            base = ord('a') if letter.islower() else ord('A')
            cypher.append(chr((ord(letter) - base + key) % 26 + base))
        else:
            cypher.append(letter)
    
    return ''.join(cypher)