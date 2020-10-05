# Problem Statement

To write a function that accept an iterable and an object and returns a new iterable with all items from the original iterable except any item at the beginning of the iterable which is equal to the object should be skipped. 

**Example**

```python
>>> lstrip([0, 0, 1, 0, 2, 3], 0)
[1, 0, 2, 3]
>>> lstrip('  hello ', ' ')
['h', 'e', 'l', 'l', 'o', ' ']
```

## Bonus 1
Return an iterator(for example a generator) from the `lstrip` function instead of a list. 

**Example** 

```python
>>> x = lstrip([0, 1, 2, 3], 0)
>>> x
<generator object <genexpr> at 0x7f0b18b0fbf8>
>>> list(x)
[1, 2, 3]
>>> list(x)
[]
```

## Bonus 2
After the function `lstrip` return a lazy iterable: allow the `lstrip` function to accept a function as it's 2nd argument which will determine whether the item should be stripped.

The function will be executed with each item individually and as long as the function returns `True` the item should be removed from the beginning of the iterable. 

**Example**

```python
>>> def is_falsey(value): return not bool(value)
>>> list(lstrip(['', 0, 1, 0, 2, 'h', ''], is_falsey))
[1, 0, 2, 'h', '']
>>> list(lstrip([-4, -2, 2, 4, -6], lambda n: n < 0))
[2, 4, -6]
```