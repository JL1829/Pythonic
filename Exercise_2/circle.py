import math

"""
class Circle(object):
    #Circle with radius, area and diameter.

    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = self.radius * 2
        self.area = math.pi * self.radius ** 2
    
    def __repr__(self):
        return f"Circle({self.radius})"
"""

class Circle(object):

    def __init__(self, radius=1):
        self.radius = radius
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"Circle({self.radius})"