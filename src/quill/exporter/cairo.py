"""
Draw to a Cairo canvas
"""


from base2 import ExporterBase2



class CairoCanvas(ExporterBase2):
    
    def __init__(self, canvas):
        self._canvas = canvas
