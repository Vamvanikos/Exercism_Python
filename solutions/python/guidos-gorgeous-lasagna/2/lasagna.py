"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME: int = 40
PREPARATION_TIME: int = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Return remaining bake time in minutes."""

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Return preparation time in minutes based on number of layers."""
    
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Return total time spent in minutes (prep + bake so far)."""
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
