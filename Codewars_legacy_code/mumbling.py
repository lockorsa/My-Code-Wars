a = 'cwAt'

def accumm(s):
    result = ''
    count = 1
    for x in s:
        y = x * count
        result += y.title() + '-'
        count += 1
    #result = result[:-1]
    return result[:-1]


def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))



#print(accum(a))
#print(accumm(a))