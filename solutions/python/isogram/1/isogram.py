def is_isogram(string: str) -> bool:
    char_list = set()
    for ch in string.lower():
        if ch == " " or ch == "-":
            continue
        if ch not in char_list:
            char_list.add(ch)
        else:
            return False
    return True
