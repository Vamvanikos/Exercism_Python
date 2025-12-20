def is_valid(isbn):
    digits = []

    for ch in isbn:
        if ch.isdigit():
            digits.append(int(ch))
        elif ch == 'X' and len(digits) == 9:
            digits.append(10)
        elif ch == '-':
            continue
        else:
            return False

    if len(digits) != 10:
        return False

    total = sum(digits[i] * (10 - i) for i in range(10))
    return total % 11 == 0