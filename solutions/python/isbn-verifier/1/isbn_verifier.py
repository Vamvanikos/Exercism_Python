def is_valid(isbn):
    mult = 10
    sum = 0
    for ch in isbn[:-1]:
        if ch.isdigit():
            sum += int(ch) * mult
            mult -= 1
        elif ch == '-':
            continue
        else:
            return False

    if mult != 1 or not isbn[-1].isdigit() and isbn[-1] != 'X':
        return False
    elif isbn[-1] == 'X':
        sum += 10
    else:
        sum += int(isbn[-1])

    return sum % 11 == 0