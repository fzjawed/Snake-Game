import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#Setting the window for the game
wnd = turtle.Screen()
wnd.title("Snake Game by Zo")
wnd.bgcolor("light blue")
wnd.setup(width=600, height=600)
wnd.tracer(0)

#Setting the text for the game
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align = "center", font=("Courier",24,"bold"))

#Creating the snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("circle")
snake.color("yellow")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

#Creating the food for the snake
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("blue")
food.penup()
food.goto(0,100)

body_seg = []

#Functions for game action

#to change directions
def move_up():
    if snake.direction != "down":
        snake.direction = "up"

def move_down():
    if snake.direction != "up" :
        snake.direction = "down"

def move_left():
    if snake.direction != "right":
        snake.direction = "left"

def move_right():
    if snake.direction != "left":
        snake.direction = "right"

#defines what happens on screen on every movement          
def movement():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)
    if snake.direction == "right": 
        snake.setx(snake.xcor() + 20)

#keyboard bindings
wnd.listen()
wnd.onkeypress(move_up, "w")
wnd.onkeypress(move_down, "s")
wnd.onkeypress(move_left, "a")
wnd.onkeypress(move_right, "d")


#Main Game loop
while True:
    wnd.update()

    #check for collisions
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"
        
        #hide the segment
        for seg in body_seg:
            seg.goto(1000,1000)
        body_seg.clear()

        #reset score
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align = "center", font=("Courier",24,"bold"))
    
    #check if snake has eaten food
    if snake.distance(food) < 20:
        #move the food to another spot
        food.goto(random.randint(-290,290),random.randint(-290,290))

        #if this does happen add a segment to the snake body
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("circle")
        new_seg.color("yellow")
        new_seg.penup()
        body_seg.append(new_seg)

        delay -= 0.001

        #increase score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align = "center", font=("Courier",24,"bold"))

    #Move the end segments to follow the others
    for i in range(len(body_seg)-1,0,-1):
        x = body_seg[i-1].xcor()
        y = body_seg[i-1].ycor()
        body_seg[i].goto(x,y)
    #Move the first segment to the head
    if len(body_seg) > 0:
        x=snake.xcor()
        y=snake.ycor()
        body_seg[0].goto(x,y)

    movement()

    #Check for body collisions
    for seg in body_seg:
        if seg.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"
            for seg in body_seg:
                seg.goto(1000,1000)
            body_seg.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,high_score),align = "center", font=("Courier",24,"bold"))


    time.sleep(delay)


wnd.mainloop()