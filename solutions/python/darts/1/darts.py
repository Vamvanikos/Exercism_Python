"""Module implementing the Darts' points system."""

def score(x, y):
    """Return points scored in a game of darts."""
    distance_sq = x*x + y*y
    if distance_sq <= 1:
        return 10
    if distance_sq <= 25:
        return 5
    if distance_sq <= 100:
        return 1
    return 0