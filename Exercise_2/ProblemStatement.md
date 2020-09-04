# Problem Statement

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

## Bonus 1

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

## Bonus 2

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

## Bonus 3
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