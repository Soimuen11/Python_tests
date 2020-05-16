import turtle
import time
import random

### WINDOW SETUP###
window = turtle.Screen()
window.title("Snake Game with vim keybindings")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

### SNAKE SETUP ###
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
# snake position / center of screen
snake.goto(0,0)
snake.direction = "stop"

# FOOD SETUP
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
snake.goto(0,0)

### SNAKE TAIL###
tail = []

### GAME INFO###
game_info = turtle.Turtle()
game_info.speed(0)
game_info.shape("square")
game_info.color("green")
game_info.penup()
game_info.hideturtle()
game_info.goto(0, 300)
game_info.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

score = 0
high_score = 0

# FUNCTIONS
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    elif snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    elif snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

### DEFINING DIRECTIONS ###
def dir_up():
    snake.direction = "up"
def dir_down():
    snake.direction = "down"
def dir_right():
    snake.direction = "right"
def dir_left():
    snake.direction = "left"

### KEYBINDINGS ###
window.listen()
window.onkeypress(dir_up, "k")
window.onkeypress(dir_down, "j")
window.onkeypress(dir_right, "l")
window.onkeypress(dir_left, "h")

# MAIN GAME LOOP
delay = 0.1
while True:
    window.update()
    # checking for collision with borders
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        #pause game for 1 sec
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"
        # hiding segments of the tail after reset
        # (moving them off screen, not deleting them !!)
        for segment in tail:
            segment.goto(1000, 1000)
        # re-init the tail
        tail = []
        # reset score 
        score = 0
        game_info.clear()
        game_info.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    # checking for collision b/w food and snake
    if snake.distance(food) < 20:
        # moving food to random x-y spot
        x = random.randrange(-290, 290)
        y = random.randrange(-290, 290)
        food.goto(x, y)
        #add a tail
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("grey")
        new_tail.penup()
        tail.append(new_tail)

        #increase score when eating food
        score += 10
        if score > high_score:
            high_score = score
            game_info.clear()
            game_info.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # move last piece of the tail first in reverse order
    for i in range(len(tail)-1, 0, -1):
        x = tail[i - 1].xcor()
        y - tail[i - 1].ycor()
        tail[i].goto(x, y)

    # move segment 0 of tail to where the head of the snake is
    if len(tail) > 0:
        x = snake.xcor()
        y = snake.ycor()
        tail[0].goto(x, y)

    move()

    # check for head collision with the body segments
    for segment in tail:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"
            #hide the tail segments
            for segment in tail:
                segment.goto(1000, 1000)
            tail = []
            score = 0
            game_info.clear()
            game_info.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
window.mainloop()
