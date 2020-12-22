import turtle
import time

#Window
win = turtle.Screen()
win.setup(width=800,height=600)
win.bgcolor("white")
win.title("Snake")
win.tracer(0)

#Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0,0)

#funcs
def move():
	snake.forward(20)
def goup():
	snake.setheading(90)
def godown():
	snake.setheading(-90)
def goleft():
	snake.setheading(-180)
def goright():
	snake.setheading(0)

#keybinds
win.listen()
win.onkeypress(goup,"Up")
win.onkeypress(godown,"Down")
win.onkeypress(goleft,"Left")
win.onkeypress(goright,"Right")


while True:
	win.update()
	snake.setx(snake.xcor())
	time.sleep(0.1)
	move()	
	snake.sety(snake.ycor())
	if (snake.xcor()>390):
		snake.goto(0,0)
	if (snake.xcor()<-390):
		snake.goto(0,0)
	if (snake.ycor()>290):
		snake.goto(0,0)
	if (snake.ycor()<-290):
		snake.goto(0,0)