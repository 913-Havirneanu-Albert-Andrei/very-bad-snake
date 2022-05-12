from Cell import Cell
import pygame
from Constants import *

class Snake:
    def __init__(self):
        self._head = Cell(420  , 220)
        self._snake = [self._head]
        self.dir = ''

    @property
    def head(self):
        return self._head

    def dead(self):
        if self._head.x > 880 or self._head.y > 480 or self._head.x < 5 or self._head.y < 5:
            return True
        for i in range(len(self._snake) - 1):
            for j in range(i + 1 , len(self._snake)):
                if self._snake[i] == self._snake[j]:
                    return True
        return False

    def show(self):
        pygame.draw.rect(wind , (0 , 255 , 0) ,pygame.Rect(self._snake[0].x , self._snake[0].y , 20 , 20))
        for s in self._snake[1:]:
            pygame.draw.rect(wind , red , pygame.Rect(s.x , s.y , 20 , 20))

    def move_right(self):
        self.dir = 'r'
        for i in range(len(self._snake) - 1 , 0 , -1):
            self._snake[i].x = self._snake[i - 1].x - 10
            self._snake[i].y = self._snake[i - 1].y
        self._snake[0].x += 10

    def move_down(self):
        self.dir = 'd'
        for i in range(len(self._snake) - 1 , 0 , -1):
            self._snake[i].x = self._snake[i - 1].x
            self._snake[i].y = self._snake[i - 1].y - 10
        self._snake[0].y += 10


    def move_up(self):
        self.dir = 'u'
        for i in range(len(self._snake) - 1, 0, -1):
            self._snake[i].x = self._snake[i - 1].x
            self._snake[i].y = self._snake[i - 1].y + 10
        self._snake[0].y -= 10

    def move_left(self):
        self.dir = 'l'
        for i in range(len(self._snake) - 1 , 0 , -1):
            self._snake[i].x = self._snake[i - 1].x + 10
            self._snake[i].y = self._snake[i - 1].y
        self._snake[0].x -= 10

    def add_cell(self):
        x_new = None
        y_new = None
        if self.dir == 'r':
            x_new = self._snake[-1].x - 20
            y_new = self._snake[-1].y
        if self.dir == 'l':
            x_new = self._snake[-1].x + 20
            y_new = self._snake[-1].y
        if self.dir == 'u':
            x_new = self._snake[-1].x
            y_new = self._snake[-1].y + 20
        if self.dir == 'd':
            x_new = self._snake[-1].x
            y_new = self._snake[-1].y - 20
        new_cell = Cell(x_new, y_new)
        self._snake.append(new_cell)