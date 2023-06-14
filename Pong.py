import turtle

wn = turtle.Screen()
wn.title("pong by Niranjan")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# score
player_a = 0
player_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)



# paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)




# ball 

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.penup()
ball.color("white")
ball.goto(0,0)
ball.dx = .1
ball.dy = .1

# pen 
pen = turtle.Turtle()
pen.speed(.1)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,250)
pen.write("Player A: 0 Player B: 0", align="center", font=("courier", 24, "normal"))






def paddle_a_up():
    y = paddle_a.ycor()
    y+= 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+= 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-= 20
    paddle_b.sety(y)

# key board binding 
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_b_up, "Up")



# main game loop 
while True:
    wn.update()
    #  move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # boarder check this will be done with the height coparison 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        player_a += 1
        pen.clear()
        pen.write("Player {}: 0 Player B: {}".format(player_a, player_b), align="center", font=("courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        player_b += 1
        pen.clear()
        pen.write("Player {}: 0 Player B: {}".format(player_a, player_b), align="center", font=("courier", 24, "normal"))
    # pabble and ball collingn 
    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor()> -350) and (ball.ycor() < paddle_a.ycor() +40  and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
