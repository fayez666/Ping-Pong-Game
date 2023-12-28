#importing the turtle module
import turtle
wind = turtle.Screen() #creating a window
wind.title("Pong by @FaYeZ") #title of the window
wind.bgcolor("black") #background color of the window
wind.setup(width=800, height=600) #size of the window
wind.tracer(0) #stops the window from updating

# madrab 1
madrab1 = turtle.Turtle() #creating a turtle object
madrab1.speed(0) #speed of animation
madrab1.shape("square") #shape of the object
madrab1.color("blue") #color of the object
madrab1.shapesize(stretch_wid=5, stretch_len=1) #size of the object
madrab1.penup() #stops the object from drawing lines
madrab1.goto(-350, 0) #position of the object

# madrab 2
madrab2 = turtle.Turtle() #creating a turtle object
madrab2.speed(0) #speed of animation
madrab2.shape("square") #shape of the object
madrab2.color("red") #color of the object
madrab2.shapesize(stretch_wid=5, stretch_len=1) #size of the object
madrab2.penup() #stops the object from drawing lines
madrab2.goto(350, 0) #position of the object

# ball
ball = turtle.Turtle() #creating a turtle object
ball.speed(0) #speed of animation
ball.shape("circle") #shape of the object
ball.color("white") #color of the object
ball.penup() #stops the object from drawing lines
ball.goto(0, 0) #position of the object
ball.dx = 1.5 #speed of the ball
ball.dy = 1.5 #speed of the ball

# Functions
def madrab1_up():
    y = madrab1.ycor() #returns the y coordinate
    y += 20 #adds 20 to the y coordinate
    madrab1.sety(y) #sets the new y coordinate

def madrab1_down():
    y = madrab1.ycor() #returns the y coordinate
    y -= 20 #adds 20 to the y coordinate
    madrab1.sety(y) #sets the new y coordinate

def madrab2_up():
    y = madrab2.ycor() #returns the y coordinate
    y += 20 #adds 20 to the y coordinate
    madrab2.sety(y) #sets the new y coordinate

def madrab2_down():
    y = madrab2.ycor() #returns the y coordinate
    y -= 20 #adds 20 to the y coordinate
    madrab2.sety(y) #sets the new y coordinate

# Score
score1 = 0
score2 = 0
score = turtle.Turtle() #creating a turtle object
score.speed(0) #speed of animation
score.color("white") #color of the object
score.penup() #stops the object from drawing lines
score.hideturtle() #hides the turtle
score.goto(0, 260) #position of the object
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal")) #writes the score on the screen



# Keyboard binding
wind.listen() #tells the window to expect keyboard input
wind.onkeypress(madrab1_up, "w") #when pressing w, madrab1_up function is called
wind.onkeypress(madrab1_down, "s") #when pressing s, madrab1_down function is called
wind.onkeypress(madrab2_up, "Up") #when pressing up arrow, madrab2_up function is called
wind.onkeypress(madrab2_down, "Down") #when pressing down arrow, madrab2_down function is called

# Main game loop
while True:
    wind.update() #updates the window

    # moving the ball
    ball.setx(ball.xcor() + ball.dx) #sets new x coordinate of the ball
    ball.sety(ball.ycor() + ball.dy) #sets new y coordinate of the ball

    # Border checking
    if ball.ycor() > 290: #top border
        ball.sety(290)
        ball.dy *= -1 #reverses the direction of the ball
    if ball.ycor() < -290: #bottom border
        ball.sety(-290)
        ball.dy *= -1 #reverses the direction of the ball
    if ball.xcor() > 390: #right border
        ball.goto(0, 0)
        ball.dx *= -1 #reverses the direction of the ball
        score1 += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() <-390: #left border
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


    # madrab and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1


