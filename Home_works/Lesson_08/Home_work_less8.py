""" Work with abstractclassmethod but pythons says this ways is deprecated
so i replace for abstractmethod, if you want try!
that's why used cls instead of self"""

import random
import turtle
from abc import ABC, abstractmethod
from random import choice

turtle.Screen().setup(500, 500)
turtle.speed(1)


class Shape(ABC):
    @abstractmethod
    def draw(cls):
        """Painting stuffs by turtle"""


class Rectangle(Shape):
    def __init__(cls, speed=1, a=150, b=75, angle=90):
        cls.speed = speed
        cls.oneside = a
        cls.secondside = b
        cls.angle = angle

    def move(cls):
        turtle.forward(cls.oneside)
        turtle.left(cls.angle)
        turtle.forward(cls.secondside)
        turtle.left(cls.angle)

    def draw(cls):
        turtle.Screen().bgcolor("black")
        turtle.color("red")
        turtle.begin_fill()
        for _ in range(2):
            cls.move()
        turtle.end_fill()


class Circle(Shape):
    """circle by turtle with random radius"""

    def draw(cls):
        turtle.Screen().bgcolor("black")
        turtle.color("yellow")
        turtle.begin_fill()
        turtle.circle(random.randint(50, 100))
        turtle.end_fill()


class Square(Shape):
    """Painting by turtle square 100x100"""

    def move(cls):
        turtle.forward(100)
        turtle.right(90)

    def draw(cls):
        for _ in range(4):
            cls.move()


def get_shape() -> Shape:
    """
    This function should return any instance of a Shape class
    In our example it is Rectangle or Circle
    """
    options: list[Shape] = [Rectangle(), Circle(), Square()]
    return choice(options)


def main():
    """Use turtle instead ;) If bad can just print"""
    """
    In Rectangle is used I'd like to see:

    ----
    |  |
    ----

    If Circle is used:
      --
     -  -
      --
    """

    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
