def is_armstrong_number(number: int) -> bool:
    if number < 0:
        return False
    
    num_of_digits: int = len(str(number))
    temp_number: int = number

    total: int = 0
    for i in range(num_of_digits):
        digit: int = temp_number % 10
        total += digit ** num_of_digits
        temp_number //= 10

    return number == total
