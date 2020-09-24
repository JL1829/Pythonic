"""
def with_previous(iterable):
    items = []
    for i in range(len(iterable)):
        if i == 0:
            items.append((iterable[i], None))
        else:
            items.append((iterable[i], iterable[i-1]))
    return items
"""

def with_previous(iterable):
    previous = None
    items = []
    for item in iterable:
        items.append((item, previous))
        previous = item
    return items
    