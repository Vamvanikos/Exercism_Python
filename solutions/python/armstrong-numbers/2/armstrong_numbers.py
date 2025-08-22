def is_armstrong_number(number: int) -> bool:
    if number < 0:
        return False
    
    str_digits: str = str(number)
    num_of_digits: int = len(str_digits)
    total: int = sum(int(digit) ** num_of_digits for digit in str_digits)

    return total == number
