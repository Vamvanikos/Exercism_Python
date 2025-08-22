MIN_SQUARE: int = 1
MAX_SQUARE: int = 64

def square(number: int) -> int:
    if not MIN_SQUARE <= number <= MAX_SQUARE:
        raise ValueError("square must be between 1 and 64")

#    return 2 ** (number - 1)
    return 1 << (number - 1)


def total() -> int:
    
    return sum(square(i) for i in range(MIN_SQUARE, MAX_SQUARE + 1))