# Pythonic Python Exercise. 
> Make your code more pythonic, modular, readability, elegant. 

## [Exercise 1](https://github.com/JL1829/Pythonic/blob/master/Exercise_1/ProblemStatement.md)
To write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together. 

It should work something like this: 
```python
>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
```

Try to solve this excise **without** using any 3rd-party libraries (for those need to use `conda` or `pip` to install)

There's two bonuses: 

### Bonus 1
Modify your `add()` function to accept non-fixed length argument (`*args`)


### Bonus 2
Raise `ValueError` if the given matrices is not the same shape. 


## [Exercise 2](https://github.com/JL1829/Pythonic/blob/master/Exercise_2/ProblemStatement.md)
Make a class that represents a Circle. 

The Circle should have a `radius`, a `diameter`, and an `area`. It should also have a nice string representation . 

**For Example**

```python
>>> c = Circle(5)
>>> c
Circle(5)

>>> c.radius
5
>>> c.diameter
10
>>> c.area
78.5398
```

Additionally the radius should default to $1$ if no `radius` is specified when you create your circle:

```python
>>> c = Circle()
>>> c.radius
1
>>> c.diameter
2
```
There are $3$ bonuses for this exercise. 

### Bonus 1

For the first bonus, make sure when the `radius` of your class changes that the `diameter` and `area` both change as well: 

### Bonus 2

For the 2nd bonus, make sure you can set the `diameter` attribute in your class and the `radius` will update accordingly. Also make sure also that you cannot set the `area`(setting area should raise an `AttributeError`):


### Bonus 3
For the 3rd bonus, make sure your `radius` cannot be set to negative number. You should raise a `ValueError` exception with the Error message: `Radius cannot be negative`. 
This mean that `diameter` cannot be negative either (and seeting `diameter` to a negative number should also raise a `ValueError`)


## [Exercise 4](https://github.com/JL1829/Pythonic/blob/master/Exercise_4/ProblemStatement.md)

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
### Bonus 1
As a bonus, make the function return an empty list for negative values of `n`:

### Bonus 2
make sure the function works with any iterable, not just sequances. 
Should make sure it don't loop at all if `n` is `0` or negative. 

See if you can make your function relatively memory efficient (if you're looping over a very long iterable, don't store the entire thing in memory)

## [Exercise 5](https://github.com/JL1829/Pythonic/blob/master/Exercise_5/ProblemStatement.md)

Write a function that accpets a sequance(a list for example) and return a new iterable(anything you can loop over) that includes a tuple of each item and the previous item(the item just before it). The first `previous item` should be `None`.

### Bonus 1
Make sure the function accept any iterable as an argument, not just a sequance(which mean you can't use index to loop).

### Bonus 2
The function can return a lazy iterator(for examaple a generator) instead of of a `list`. 

### Bonus 3
Allow the function to accept an optional `fillvalue` keywork-only argument(default to `None`)

This new argument should be allowed as a keyword argument. The following should raise error: 
```python
>>> list(with_previous([1, 2, 3], 0))
Traceback (most recent call last): File "", line 1, in TypeError: with_previous() takes 1 positional argument but 2 were given
```
