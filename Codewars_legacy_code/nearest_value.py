

def nearest_value(values: set, one: int) -> int:
    diff = None
    result = None

    for value in values:
        if value < one:
            if diff == None or one-value <= diff:
                diff = one - value
                result = value
        elif value >= one:
            if diff == None or value-one < diff:
                diff = value - one
                result = value
    return result


a, b, c, e = {4, 7, 10, 11, 12, 17}, 0, 6, 18

print(nearest_value(a, b), nearest_value(a, c), nearest_value(a, e))

