a, b, c, d, e = '', 'a', 'abc', 'abcd', 'abcdf'


def split_pairs(a):
    a += '_' * (len(a) % 2)
    return [a[i:i+2] for i in range(0, len(a), 2)]


print(split_pairs(a), split_pairs(b), split_pairs(c), split_pairs(d), split_pairs(e))
