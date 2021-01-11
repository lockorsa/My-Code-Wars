
def two_sum(numbers, target):
    result = []
    for first_index, first in enumerate(numbers):
        for second_index, second in enumerate(numbers):
            if first + second == target and not first_index == second_index:
                    return [first_index, second_index]



print(two_sum([2,2,3], 4))
