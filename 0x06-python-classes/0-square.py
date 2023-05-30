#!/usr/bin/python3
class Square:
    """Class Square that defines a square.
    """
    def __init__(self, side_length):
        self.side_length = side_length
    """Initializes an instance variable
    """
    def area(self):
        return self.side_length ** 2
    """to calculate the permitere of the square
    """
    def perimeter(self):
        return 4 * self.side_length
