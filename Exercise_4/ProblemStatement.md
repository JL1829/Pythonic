# tail

Write a function that takes a sequence (like a `list`, `string` or `tuple`) and a number `n` and returns the last `n` elements from the given sequance, as a `list`. 

For Example:
```python
>>> tail([1, 2, 3, 4, 5], 3)
[3, 4, 5]
>>> tail('hello', 2)
['l', 'o']
>>> tail('hello', 0)
[]
```

## Bonus 1
As a bonus, make the function return an empty list for negative values of `n`:
```python
>>> tail('hello', 2)
[]
```

## Bonus 2
make sure the function works with any iterable, not just sequances. 
For example:
```python
>>> squares = (n**2 for n in range(10))
>>> tail(squares, 3)
[49, 64, 81]
```

Should make sure it don't loop at all if `n` is `0` or negative. 

See if you can make your function relatively memory efficient (if you're looping over a very long iterable, don't store the entire thing in memory)
