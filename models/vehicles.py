# creating class Vehicle
class Vehicle:
    #Private members
    __regno = None
    __color = None
    #constructor
    def __init__(self, regno, color):
        self.__regno = regno
        self.__color = color

    def get_regno(self):
        return self.__regno

    def get_color(self):
        return self.__color

    def get_info(self):
        return [self.__regno, self.__color]
