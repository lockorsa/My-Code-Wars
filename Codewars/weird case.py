from itertools import cycle


def to_weird_case(string):
    result = ''
    for i in string.split():       # i = [Weird, string, case]
        flag = True
        for x in i:                # x = [w, e, i, r, d]
            if flag:
                result += x.upper()
            else:
                result += x.lower()
            flag = not flag
        result += ' '
    return result[:-1]

a = 'Weird string case'
print(to_weird_case(a))
