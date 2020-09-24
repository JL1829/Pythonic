# Problem Statement

Write a function that accpets a sequance(a list for example) and return a new iterable(anything you can loop over) that includes a tuple of each item and the previous item(the item just before it). The first `previous item` should be `None`.

**For Example**

```python
>>> with_previous('hello')
[('h', None), ('e', 'h'), ('l', 'e'), ('l', 'l'), ('o', 'l')]
>>> with_previous([1, 2, 3])
[(1, None), (2, 1), (3, 2)]
```

There are three option bonues for tis exercise.

## Bonus 1
Make sure the function accept any iterable as an argument, not just a sequance(which mean you can't use index to loop).

Here's an example witha generator expression, which is a lazy iterable: 
```python
>>> with_previous(n** for n in [1, 2, 3])
[(1, None), (4, 1), (9, 4)]
```

## Bonus 2
The function can return a lazy iterator(for examaple a generator) instead of of a `list`. 

This should allow the `with_previous` function to accept infinitely long iterables. If the function returns an iterabor, the below should work: 
```python
>>> next(with_previous([1, 2, 3]))
(1, None)
```

## Bonus 3
Allow the function to accept an optional `fillvalue` keywork-only argument(default to `None`)
The below should work:
```python
>>> list(with_previous([1, 2, 3], fillvalue=0))
[(1, 0), (2, 1), (3, 2)]
```

This new argument should be allowed as a keyword argument. The following should raise error: 
```python
>>> list(with_previous([1, 2, 3], 0))
Traceback (most recent call last): File "", line 1, in TypeError: with_previous() takes 1 positional argument but 2 were given
```
