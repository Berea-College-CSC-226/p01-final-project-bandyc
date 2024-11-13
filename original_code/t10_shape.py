######################################################################
# Author: Joyce Nimely, Cody Bandy
# Username: bandyc-nimelyj
#
# Assignment: T10: Intro to Classes
#
# Purpose: A class for creating shapes collaborating with the Point class""
######################################################################

####################################################################################


import turtle
from t10_point import Point


class Shape:
    """A class to manufacture Shapes.
         -start_point (Point): The starting location for drawing the shape.
        - num_sides (int): Number of sides in the polygon.
        - side_length (int): Length of each side (limited by max_size)."""
    max_size = 100

    def __init__(self, start_point, num_sides, side_length):   #initializes a Shape object.
        """ Initializes the shape object
     parameters:
          start_point (Point): The starting location for drawing the shape.
           num_sides (int): Number of sides in the polygon.
    side_length (int): Length of each side (limited by max_size)."""

        self.start_point = start_point
        self.num_sides = num_sides
        self.side_length = min(side_length, Shape.max_size)
        self.turtley = turtle.Turtle()

    def draw_shape(self, r=255, g=255, b=255,):
        angle = 360 / self.num_sides
        self.turtley.penup()
        self.turtley. goto(self.start_point.x, self.start_point.y )
        self.turtley.pendown()
        self.turtley.color(r /255, g / 255, b / 255)


        for _ in range(self.num_sides):
            self.turtley.forward(self.side_length)
            self.turtley.left(angle)

if __name__ == "__main__":
        start = Point(0, 0)
        shape = Shape(start, 5, 50)
        shape.draw_shape(255, 255, 255)
        turtle.done()











