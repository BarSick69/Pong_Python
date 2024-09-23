import turtle
import time
import winsound
wn = turtle.Screen()
wn.title("Pong by Yagan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)



# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 300
ball.dy = 300
score_a = 0
score_b = 0
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# Main game loop
prev_time = time.time()
while True:
    wn.update()
    current_time = time.time()
    delta_time = current_time - prev_time
    prev_time = current_time  # Update the previous time to the current time
    pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    # Move the ball with respect to the delta time

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)
    ball.setx(ball.xcor() + ball.dx * delta_time)
    ball.sety(ball.ycor() + ball.dy * delta_time)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        pen.clear()
        score_a += 1
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0, 0)
        pen.clear()
        score_b += 1
        ball.dx *= -1
    
    if ball.xcor() < -330 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-330)
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    elif ball.xcor() > 330 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if score_a == 5:
        wn.clear()
        pen.clear()
        pen.goto(0, 0)
        pen.write("Player A wins", align="center", font=("Courier", 24, "normal"))
        wn.bgcolor("black")
        wn.update()
        time.sleep(3)
        break
    if score_b == 5:
        wn.clear()
        pen.clear()
        pen.goto(0, 0)
        pen.write("Player B wins", align="center", font=("Courier", 24, "normal"))
        wn.bgcolor("black")
        wn.update()
        time.sleep(3)
        break
    
    
   
    