# Pythonic Python Exercise. 
> Make your code more pythonic, modular, readability, elegant. 

## Exercise 1
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

```python
>>> matrix1 = [[1, 9], [7, 3]]
>>> matrix2 = [[5, -4], [3, 3]]
>>> matrix3 = [[2, 3], [-3, 1]]
>>> add(matrix1, matrix2, matrix3)
[[8, 8], [7, 7]]
```

### Bonus 2
Raise `ValueError` if the given matrices is not the same shape. 
```python
>>> add([[1, 9], [7, 3]], [[1, 2], [3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "add.py", line 10, in add
    raise ValueError("Given matrices are not the same size.")
ValueError: Given matrices are not the same size.
```

## Exercise 2
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

```python
>>> c = Circle(2)
>>> c.radius
2
>>> c.diameter
4

>>> c.radius = 1
>>> c.diameter
2
>>> c.area
3.1415926
>>> c
Circle(1)
```

### Bonus 2

For the 2nd bonus, make sure you can set the `diameter` attribute in your class and the `radius` will update accordingly. Also make sure also that you cannot set the `area`(setting area should raise an `AttributeError`):

```python
>>> c = Circle(1)
>>> c.diameter = 4
>>> c.radius
2.0
>>> c.area = 45.678
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 16, in radius
AttributeError: can't set attribute
```

### Bonus 3
For the 3rd bonus, make sure your `radius` cannot be set to negative number. You should raise a `ValueError` exception with the Error message: `Radius cannot be negative`. 

```python
>>> c = Circle(5)
>>> c.radius = 3
>>> c.radius = -2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 27, in radius
    raise ValueError("Radius cannot be negative")
ValueError: Radius cannot be negative
>>> c = Circle (-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 27, in radius
    raise ValueError("Radius cannot be negative")
ValueError: Radius cannot be negative
```
This mean that `diameter` cannot be negative either (and seeting `diameter` to a negative number should also raise a `ValueError`)