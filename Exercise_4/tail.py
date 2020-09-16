def tail(iterable, index):
    if index > 0:
        return [i for i in iterable][-index:]
    else:
        return []
