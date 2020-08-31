#! /Users/johnnylu/anaconda3/envs/py377/bin/python

# matrix1 = [[1, 2, 3], [4, 5, 6]]
# matrix2 = matrix1

# result = add(matrix1, matrix2)
# print(result)
"""
def add(*args):
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*args)
    ]
"""
from itertools import zip_longest

def add(*args):
    try:
        return [
            [sum(values) for values in zip_longest(*rows)]
            for rows in zip_longest(*args)
        ]
    except TypeError as Error:
        raise ValueError("Given matrices are not the same size.") from Error
