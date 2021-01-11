a = 100100
b = 0
c = 1

"""
def end_zeros(num: int) -> int:
    result = 0
    for x in str(num):
        if x == '0':
            result += 1
        elif int(x) > 0:
            result = 0
    return result
"""

def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))
          #len(str(num)) - len(str(num).rstrip(‘0’))


print(end_zeros(a))
print(end_zeros(b))
print(end_zeros(c))