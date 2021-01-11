a = 'credit card number'

"""
def maskify(cc):
    result = ''
    x = 0
    while x < len(cc):
        if len(cc) - x <= 4:
            result += cc[x]
        else:
            result += '#'
        x += 1
    return result
"""

def maskify(cc):
    return '#'*(len(cc)-4) + cc[-4:]

print(maskify(a))









