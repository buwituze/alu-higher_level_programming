#!/usr/bin/python3
"""Define a rectangle based on 7-base_geometry.py.

Attributes:
    width : width of the rec.
    height: height of the rec.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Creates new instances of Rectangle.

        Args:
            width : width of rect.
            height : height of rec.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
