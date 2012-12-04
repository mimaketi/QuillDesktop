"""
A pen stroke
"""


class Stroke:
    
    def __init__(self, x_coordinates, y_coordinates, pressure=None):
        assert len(x_coordinates)==len(y_coordinates)
        self.x = x_coordinates
        self.y = y_coordinates
        self.p = pressure
