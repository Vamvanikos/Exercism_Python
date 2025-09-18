def translate_word(word):
    word_lower = word.lower()
    if word_lower[0] in 'aeiou' or \
       word_lower.startswith(("xr", "yt")):
        return word + "ay"

    move = 0
    while move < len(word):
        if word_lower[move : move + 2] == "qu":
            move += 2
            break
        if word_lower[move] in 'aeiou' or \
           word_lower[move] == "y" and move != 0:
            break
        move += 1

    return word[move:] + word[0:move] + "ay"

def translate(text):

    return " ".join(translate_word(word) for word in text.split())