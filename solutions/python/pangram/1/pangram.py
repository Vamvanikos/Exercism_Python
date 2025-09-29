import string

def is_pangram(sentence: str) -> bool:
    alphabet = set(string.ascii_lowercase)

    return alphabet.issubset(set(sentence.lower()))
