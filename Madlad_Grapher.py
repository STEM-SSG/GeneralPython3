# Author        Calvin Johnson
# Date          2021-08-07
# Revised       2021-08-07
# Variant       01.0
# Filename      Madlad_Grapher.py
# Description   Completed Madlad Grapher Program
# _______	________

import turtle           # Allows the use of the turtle


# User functions
# --------------

'''
draws a square at the given (screen_x, screen_y) coordinate, with the specified side width
uses a loop to draw the sides, thus simplifying code
'''
def draw_square(screen_x, screen_y, width):

    # use the preexisting grid_turtle variable
    global grid_turtle

    # move penup
    grid_turtle.penup()

    # go to specified position
    grid_turtle.goto(screen_x, screen_y)
    grid_turtle.pendown()

    # face each direction and go forward
    # this draws each side of the square
    for heading in [0, 90, 180, 270]:
        grid_turtle.setheading(heading)
        grid_turtle.forward(width)

    # finished drawing, so penup so we don't draw when we move next
    grid_turtle.penup()

'''
draws a grid centered at the origin (centre of screen),
with grid_width and grid_height being how many squares in the positive x and y direction,
and tile_width is the width of each grid square.

NOTE: also draws in the negative x and y direction, using same number of squares as is in positive x and y
'''
def draw_grid(grid_width, grid_height, tile_width):
    # use the preexisting grid_turtle variable
    global grid_turtle

    # draw grid, set outline colour
    grid_turtle.color("light grey")

    # loop through each grid square location and draw it
    for x in range(-grid_width, grid_width):
        for y in range(-grid_height, grid_height):
            draw_square(x*tile_width, y*tile_width, tile_width)

    # draw axis
    grid_turtle.color("black")
    draw_axis(grid_width, grid_height, tile_width)

'''
draws the grid axis centered at the origin corresponding to
the grid given by grid_width, grid_height, and tile_width
(as seen in draw_grid())
'''
def draw_axis(grid_width, grid_height, tile_width):
    # use the preexisting grid_turtle variable
    global grid_turtle
    grid_turtle.penup()    

    # horizontal axis

    # go to left point of horizontal axis, and label it
    grid_turtle.goto(-grid_width * tile_width, 0)
    grid_turtle.write(str(-grid_width), align = 'center', font = ("times", 22, 'bold'))

    # move to right side of axis and trace path to draw the axis line
    grid_turtle.pendown()
    grid_turtle.setheading(0)
    grid_turtle.forward(2 * grid_width * tile_width)
    # label right side point on axis
    grid_turtle.write(str(grid_width), align = 'center', font = ("times", 22, 'bold'))
    # pen up so we don't draw extra line when moving to vertical axis
    grid_turtle.penup()

    # vertical axis

    # go to bottom point of vertical axis, and label it
    grid_turtle.goto(0, -grid_height * tile_width)

    # move to top of axis and trace path to draw the axis line
    grid_turtle.write(str(-grid_height), align = 'center', font = ("times", 22, 'bold'))
    grid_turtle.pendown()
    grid_turtle.setheading(90)
    grid_turtle.forward(2 * grid_width * tile_width)
    # label top point on axis
    grid_turtle.write(str(grid_height), align = 'center', font = ("times", 22, 'bold'))

    # pen up so we don't draw in the next function accidentally
    grid_turtle.penup()

    
'''
draws a point at the given (grid_x, grid_y) pair
'''
def plot_point(grid_x, grid_y, grid_width, grid_height, tile_width, color, shape):
    # use the preexisting grid_turtle variable
    global grid_turtle
        
    # make sure we don't plot off the grid we drew
    if (grid_x >= -grid_width and grid_x <= grid_width) and (grid_y >= -grid_height and grid_y <= grid_height):
        # make sure pen is up
        grid_turtle.penup()

        # set colour and shape appropriately
        grid_turtle.color(color)
        grid_turtle.shape(shape)

        screen_x = grid_x * tile_width
        screen_y = grid_y * tile_width

        # go to correct grid point and stamp turtle
        grid_turtle.goto(screen_x, screen_y)
        grid_turtle.stamp()

'''
opens a file for reading, and parses each line into an x,y pair, then returns the data
'''
def read_point_data(file_name):
    # declare an empty list to store all the data in
    data = []

    try:
        # open the file in reading mode
        data_file = open(file_name, mode='r')
    except IOError:
        # file doesn't exist
        print("File not found:", file_name)
        # return empty data
        return data

    # read until the line is empty i.e. we've reached the end of file
    line = data_file.readline()  
    while line != "":
        try:
            # each line should be in the form "x,y" 
            values = line.split(",")
            
            # convert to int and add to list
            data.append([float(values[0]), float(values[1])])
        except ValueError:
            # ValueError: One of the values wasn't a number
            print("Invalid data line:", line)
        except IndexError:            
            # IndexError: Line is an incorrect format
            print("Invalid data line:", line)

        # read next line for the next iteration
        line = data_file.readline()

    # return parsed data
    return data

'''
plots all points located in the given file
'''
def plot_file_data(grid_width, grid_height, tile_width, file_name):
    # read data from the file
    data = read_point_data(file_name)

     # loop through each data point and plot it
    for point in data:
        grid_x = point[0]
        grid_y = point[1]
        plot_point(grid_x, grid_y, grid_width, grid_height, tile_width, "orange", "circle")


# Main program starts here
# ------------------------
if __name__ == '__main__':
    from setup import setup
    turtle_window = setup("Madlad Grapher™")

    # turn tracer off to draw grid instantly
    grid_turtle = turtle.Turtle()
    # change speed to draw faster when tracer is on
    grid_turtle.speed('fastest')

    # set grid width and height, and size of each grid square
    grid_width = 5
    grid_height = 5
    tile_width = 50

    # file to read plotting data out of
    data_filename = "Data.txt"

    # draw grid
    draw_grid(grid_width, grid_height, tile_width)

    # plot data read from the file
    plot_file_data(grid_width, grid_height, tile_width, data_filename)
    plot_point(0.5, 0.5, 5,5, 50,"red", "turtle")

    # Draw all the code to the screen
    turtle_window.mainloop()

# Exit the program
