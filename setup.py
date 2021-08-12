# Author        Tristan Bellingham
# Date          2021-07-30
# Revised       2021-08-02
# Variant       01.0
# Filename      setup.py
# Description   Setup code for module 2 code
#               QUT Student Sucess Group - General Python modules

import turtle


def setup(title: str) -> turtle.TurtleScreen:
    # Control the size of the drawing space. Units are Pixels.
    canvas_height = 600
    canvas_width = 800

    drawing_delay = 1       # Small delay for dramatic effect

    # Setup the canvas for the turtle drawing.
    turtle.setup(canvas_width, canvas_height)

    # Create the place to use the turtle for drawing.
    turtle_window = turtle.Screen()

    # Set the title at the top of the window
    turtle_window.title(title)
    turtle.tracer(False)

    return turtle_window