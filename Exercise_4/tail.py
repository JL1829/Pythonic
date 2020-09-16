def tail(iterable, index):
    if index > 0:
        return [i for i in iterable][-index:]
    else:
        return []

"""
def tail(iterable, index):
    if index < 0:
        return []
    elif index == 0:
        return []
    else:
        return list(list(iterable)[-index:])
"""