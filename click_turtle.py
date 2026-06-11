import turtle
import random

# Set up the screen window
window = turtle.Screen()

# Create a visible turtle object
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(4)  # Make it larger and easier to click

colors = ["red", "blue", "green", "purple", "orange"]
my_turtle.color(random.choice(colors))

# Define the click handler function (Must accept x, y)
def handle_click(x, y):
    my_turtle.right(90)

# Bind the function to the turtle object click event
my_turtle.onclick(handle_click)

# Keep the window open and listening for events
window.mainloop()
