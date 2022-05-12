class Cell:
    def __init__(self , x , y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    @x.setter
    def x(self , value):
        self._x = value

    @y.setter
    def y(self , value):
        self._y = value

    def __str__(self):
        return f"{self.x} , {self.y}"

    def __eq__(self , other):
        return self.x == other.x and self.y == other.y