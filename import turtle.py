import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# Helper function to draw rectangle
def draw_rectangle(color, width, height):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Draw shield outline (simplified)
t.penup()
t.goto(-50, 150)
t.pendown()
t.begin_fill()
t.fillcolor("gold")
t.goto(50, 150)
t.goto(70, 100)
t.goto(70, -100)
t.goto(0, -150)
t.goto(-70, -100)
t.goto(-70, 100)
t.goto(-50, 150)
t.end_fill()

# Red and yellow stripes (Catalonia flag)
stripe_width = 20
t.penup()
t.goto(-60, 100)
t.setheading(0)

for i in range(4):
    t.pendown()
    draw_rectangle("red", stripe_width, 100)
    t.penup()
    t.forward(stripe_width)
    t.pendown()
    draw_rectangle("yellow", stripe_width, 100)
    t.penup()
    t.forward(stripe_width)

# English cross (Saint George)
t.goto(-30, 100)
t.setheading(0)
t.pendown()
t.fillcolor("white")
t.begin_fill()
draw_rectangle("white", 60, 60)
t.end_fill()

# Vertical red line
t.penup()
t.goto(-10, 100)
t.pendown()
draw_rectangle("red", 20, 60)

# Horizontal red line
t.penup()
t.goto(-30, 70)
t.pendown()
draw_rectangle("red", 60, 20)

# Hide turtle and end
t.hideturtle()
turtle.done()
