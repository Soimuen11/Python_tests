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
snake.shape("circle")
snake.color("purple")
snake.penup()
# snake position / center of screen
snake.goto(0,0)
snake.direction = "stop"

# FOOD SETUP
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("red")
food.penup()
snake.goto(0,0)

### SNAKE TAIL###
tail = []

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

    # checking for collision b/w food and snake
    if snake.distance(food) < 20:
        # moving food to random x-y spot
        x = random.randrange(-290, 290)
        y = random.randrange(-290, 290)
        food.goto(x, y)
        #add a tail
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("circle")
        new_tail.color("orange")
        new_tail.penup()
        tail.append(new_tail)

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
    time.sleep(delay)
window.mainloop()
