from typing import Iterable

a = [1, 2, 3, 4, 5]
b = [1, 1, 2, 4, 2, 3, 4]
c = [1, 1, 5, 6, 7]
d = 2

def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        sep = items.index(border)
        return items[sep:]
    return items
   #return items[items.index(border):] if border in items else items


print(remove_all_before(a, d))
print(remove_all_before(b, d))
print(remove_all_before(c, d))