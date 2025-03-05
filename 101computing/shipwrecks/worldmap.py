import turtle

#Display information on world map using Python Turtle
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
#Load the world map picture
screen.bgpic("images/world-map.gif")

myPen = turtle.Turtle()
myPen.penup()
myPen.color("yellow")
myPen.setheading(45)

def plot(longitude, latitude):
   myPen.goto(longitude, latitude)