import turtle
import random
import random

# create window
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("Black")
window.setup(width=800, height=600)
window.cv._rootwindow.resizable(False, False)
#stop window from updating
window.tracer(0)

# Score counting
score_a=0
score_b=0

# Paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(5)
paddle_a.shape("square")
paddle_a.color("White")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("White")
paddle_b.shapesize(stretch_wid=7, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
# Set ball speed based on a random tick generator
ball.speed(random.randint(1, 10))
ball.shape("square")
ball.color("White")
ball.penup()
ball.goto(0, 0)

# Scoring pen
pen = turtle.Turtle()
pen.speed(2)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 210)
pen.write("0     0", align="center", font=("Courier", 50, "normal"))


#screen devider
sd = turtle.Turtle()
sd.color("white")
sd.shape("square")
sd.penup()
sd.shapesize(stretch_wid=50, stretch_len=1)

#ball moving SPEED
ball.dx = 10 / 30  # Speed adjusted for 30 FPS
ball.dy = 10 / 30  # Speed adjusted for 30 FPS

# Paddle moving SPEED
paddle_b.dy = 0.2

# Flags for paddle movement
paddle_a_up_pressed = False
paddle_a_down_pressed = False

# Functions to set flags
def paddle_a_up_press():
    global paddle_a_up_pressed
    paddle_a_up_pressed = True

def paddle_a_up_release():
    global paddle_a_up_pressed
    paddle_a_up_pressed = False

def paddle_a_down_press():
    global paddle_a_down_pressed
    paddle_a_down_pressed = True

def paddle_a_down_release():
    global paddle_a_down_pressed
    paddle_a_down_pressed = False

# Functions
# Going up Paddle b
def paddle_b_up():
     y = paddle_b.ycor()
     y += 20
     paddle_b.sety(y)

     
# Going down paddle b
def paddle_b_down():
     y = paddle_b.ycor()
     y -= 20
     paddle_b.sety(y)
     
# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up_press, "w")
window.onkeyrelease(paddle_a_up_release, "w")
window.onkeypress(paddle_a_down_press, "s")
window.onkeyrelease(paddle_a_down_release, "s")

#Main game loop
while True:
     window.update()

     # Move paddle A continuously if keys are pressed
     if paddle_a_up_pressed:
         y = paddle_a.ycor()
         y += 2 #speed of the paddle
         paddle_a.sety(y)

     if paddle_a_down_pressed:
         y = paddle_a.ycor()
         y -= 2 #speed of the paddle
         paddle_a.sety(y)
     
     # move the ball
     ball.setx(ball.xcor() + ball.dx)
     ball.sety(ball.ycor() + ball.dy)
     
     #move the paddle up
     paddle_b.sety(paddle_b.ycor() + paddle_b.dy)
     
     # Border check and moving AI (PADDLE B)
     if paddle_b.ycor() > 290:
          paddle_b.sety(290)
          paddle_b.dy *= -1
     
     if paddle_b.ycor() < -290:
          paddle_b.sety(-290)
          paddle_b.dy *= -1
     
     
     
     #check borders for paddle a
     if paddle_a.ycor() > 260:
          paddle_a.goto(-350, 260)
     else:
          if paddle_a.ycor() < -260:
               paddle_a.goto(-350, -260)
               
    
     #check border for paddle b
     if paddle_b.ycor() > 290:
          paddle_b.goto(350, 290)
     else:
          if paddle_b.ycor() < -290:
               paddle_b.goto(350, -290)
      
          
     #check the BORDERs for ball
     if ball.ycor() > 290:
          ball.sety(290)
          ball.dy*= -1
          
     if ball.ycor() < -290:
          ball.sety(-290)
          ball.dy *= -1
          
     if ball.xcor() > 390:
          ball.goto(0, 0)
          ball.dx *= -1
          score_a +=1
          pen.clear()
          pen.write("{}     {}" .format(score_a, score_b), align="center", font=("Courier", 50, "normal"))
          
          
     if ball.xcor() < -390:
          ball.goto(0, 0)
          ball.dx *= 1
          score_b +=1
          pen.clear()
          pen.write("{}     {}" .format(score_a, score_b), align="center", font=("Courier", 50, "normal"))
          
          
     # Paddle and ball collision

     # Collision with Paddle B
     if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 
                                                       and ball.ycor() > paddle_b.ycor() - 50):
          ball.setx(340)
          ball.dx *= -1

     # Collision with Paddle A
     if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 
                                                         and ball.ycor() > paddle_a.ycor() - 50):
          ball.setx(-340)
          ball.dx *= -1






