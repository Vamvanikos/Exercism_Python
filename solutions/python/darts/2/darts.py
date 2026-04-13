"""Module implementing the Darts' points system."""

def score(x_pos, y_pos):
    """Return points scored in a game of darts."""
    distance_sq = x_pos*x_pos + y_pos*y_pos
    if distance_sq <= 1:
        return 10
    if distance_sq <= 25:
        return 5
    if distance_sq <= 100:
        return 1
    return 0