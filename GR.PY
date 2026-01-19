import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Graphics Example")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")

# Draw a pattern
colors = ["red", "yellow", "green", "blue", "purple", "orange"]

for i in range(100):
    pen.color(colors[i % len(colors)])  # Change colors
    pen.forward(i * 4)  # Move forward
    pen.right(91)       # Turn angle

# Finish
turtle.done()