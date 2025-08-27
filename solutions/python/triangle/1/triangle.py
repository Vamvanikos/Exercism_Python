def is_not_triangle(sides: tuple) -> bool:
    return any(side <= 0 for side in sides) or \
           sides[0] + sides[1] < sides[2] or \
           sides[1] + sides[2] < sides[0] or \
           sides[0] + sides[2] < sides[1]

def equilateral(sides: tuple) -> bool:
    return not is_not_triangle(sides) and \
           sides[0] == sides[1] == sides[2]

def isosceles(sides: tuple) -> bool:
    return not is_not_triangle(sides) and \
           (sides[0] == sides[1] or \
            sides[0] == sides[2] or \
            sides[1] == sides[2])

def scalene(sides: tuple) -> bool:
    return not is_not_triangle(sides) and \
           sides[0] != sides[1] != sides[2] != sides[0]# and \
           #sides[0] != sides[2]
