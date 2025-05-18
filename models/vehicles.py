# creating class Vehicle
class Vehicle:
    def __init__(self, regno, color):
        self._regno = regno
        self._color = color

    @property
    def regno(self):
        return self._regno
    @property
    def color(self):
        return self._color
    @regno.setter
    def regno(self, regno):
        self._regno = regno
    @color.setter
    def color(self, color):
        self._color = color
