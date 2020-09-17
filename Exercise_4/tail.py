from collections import deque

def tail(iterable, index):
    if index > 0:
        # the follow script will still create a full list of iterable
        # it's not memory efficient
        # write new one
        
        # return [i for i in iterable][-index:]
        
        # we can use deque() to control the length of the list
        return list(deque(iterable, maxlen=index))
    else:
        return []
