import random
import pygame
from Constants import *

"""
    Apple class
"""

class Apple:
    def __init__(self):
        """
        Initializez the apple with a random value multiple of 10
        """
        self._x = random.randint(1 , 88) * 10
        self._y = random.randint(1 , 48) * 10

    def change_coords(self):
        """
        Just changes the values
        :return: None
        """
        self._x = random.randint(1 , 88) * 10
        self._y = random.randint(1 , 48) * 10

    @property
    def x(self):
        """
        Getter for x value
        :return: Int
        """
        return self._x

    @property
    def y(self):
        """
        Getter for y value
        :return: Int
        """
        return self._y

    def show(self):
        """
        Drawing the apple at the coords x and y
        :return:
        """
        pygame.draw.rect(wind , white , pygame.Rect(self._x , self._y , 20  ,20))