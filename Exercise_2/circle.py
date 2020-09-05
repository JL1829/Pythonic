import math

class Circle(object):

    def __init__(self, radius=1):
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError('Radius cannot be negative')
    
    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property 
    def radius(self):
        return self._radius
    
    @radius.setter 
    def radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            raise ValueError('radius cannot be negative')
