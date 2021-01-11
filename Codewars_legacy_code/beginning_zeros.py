a, b, c, d, e = '0000', '001', '100', '100100', '012345679'


def beginning_zeros(number: str) -> int:
    result = 0
    for i in number:
        if i == '0':
            result += 1
        else:
            return result
    return result
   #return len(number) - len(number.lstrip('0'))

print(beginning_zeros(a), beginning_zeros(b), beginning_zeros(c), beginning_zeros(d), beginning_zeros(e))
