import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Brick Bounce")
screen.tracer(0)

# Paddle setup
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Paddle movement
def paddle_left():
    x = max(paddle.xcor() - 60, -350)
    paddle.setx(x)

def paddle_right():
    x = min(paddle.xcor() + 60, 350)
    paddle.setx(x)

# Scoreboard
def update_scoreboard():
    score_display.clear()
    score_display.write(f"Score: {score} Lives: {lives}", align="left", font=("Courier", 16, "normal"))

# Level reset
def reset_level():
    ball.goto(0, -230)
    ball.dx *= 1.1
    ball.dy *= 1.1
    paddle.goto(0, -250)

# Brick creation
def create_new_level():
    bricks.clear()
    for row in range(rows):
        for col in range(columns):
            brick = turtle.Turtle()
            brick.color("blue")
            brick.shape("square")
            brick.shapesize(stretch_wid=0.5, stretch_len=3.5)
            brick.penup()
            x = start_x + col * brick_width
            y = start_y - row * brick_height
            brick.goto(x, y)
            bricks.append(brick)

# Power-up mechanics
def drop_power_up():
    if not power_up_active:
        power_up.goto(brick.xcor(), brick.ycor())
        power_up.showturtle()

def activate_power_up():
    paddle.shapesize(stretch_wid=1, stretch_len=8)
    power_up.hideturtle()

def check_power_up():
    global power_up_active
    power_up.sety(power_up.ycor() - 5)
    if power_up.ycor() < -300:
        power_up.hideturtle()
    elif paddle.distance(power_up) < 50:
        activate_power_up()

# Game over or victory message
def display_message(message):
    game_over = turtle.Turtle()
    game_over.color("red")
    game_over.penup()
    game_over.hideturtle()
    game_over.goto(0, 0)
    game_over.write(message, align="center", font=("Courier", 24, "bold"))
    screen.update()


# Keyboard bindings
screen.listen()
screen.onkey(paddle_left, "Left")
screen.onkey(paddle_right, "Right")

# Ball setup
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(0, -230)
ball.dx = 2
ball.dy = 2
ball.showturtle()

# Brick setup
bricks = []
rows = 5
columns = 5
brick_height = 20
brick_width = 80
start_x = -320
start_y = 200
create_new_level()

# Score and lives
score = 0
lives = 3

# Score display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-350, 260)
update_scoreboard()

# Power-up setup
power_up = turtle.Turtle()
power_up.shape("circle")
power_up.color("yellow")
power_up.penup()
power_up.speed(0)
power_up.hideturtle()
power_up_active = False

level = 1
running = True

while running:
    screen.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -300:
        lives -= 1
        update_scoreboard()
        if lives == 0:
            display_message("Game Over!")
            running = False
        else:
            reset_level()

    if -240 < ball.ycor() < -230 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
        ball.dy *= -1

    for brick in bricks:
        if brick.isvisible() and (brick.xcor() - 40 < ball.xcor() < brick.xcor() + 40) and (brick.ycor() - 10 < ball.ycor() < brick.ycor() + 10):
            ball.dy *= -1
            brick.hideturtle()
            bricks.remove(brick)
            score += 1
            update_scoreboard()
            break

    if not bricks:
        level += 1
        create_new_level()
        reset_level()

screen.mainloop()
