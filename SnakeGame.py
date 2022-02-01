import turtle
import time
import random

delay = 0.1
score = 0
highScore = 0

screen = turtle.Screen()
screen.setup(650,650) #.setup(,) cambio el tamaño de la pantalla
screen.bgcolor("gray")
screen.title("Snake Game by Lordlez")

snake = turtle.Turtle()
snake.speed(1)
snake.shape("square")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop' 
snake.color("green") 

food = turtle.Turtle()
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0,100)
food.speed(0)

body = []

text = turtle.Turtle()
text.speed(0)
text.color("black")
text.penup()
text.hideturtle()
text.goto(0,-260)
text.write("Marcador: 0 \tMarcador mas alto: 0")

def up():
    snake.direction = 'up'

def down():
    snake.direction = 'down'

def right():
    snake.direction = 'right'

def left():
    snake.direction = 'left'


def movement():
    if snake.direction == 'up':
        y = snake.ycor() #.ycor() me da la coordenada del eje Y
        snake.sety(y+20)
    if snake.direction == 'down':
        y = snake.ycor() #.ycor() me da la coordenada del eje Y
        snake.sety(y-20)
    if snake.direction == 'right':
        x = snake.xcor() #.ycor() me da la coordenada del eje Y
        snake.setx(x+20)
    if snake.direction == 'left':
        x = snake.xcor() #.ycor() me da la coordenada del eje Y
        snake.setx(x-20)

screen.listen() #.listem() escucha lo que mandemos por teclado
screen.onkeypress(up, "Up") #.keypress() toma la tecla
screen.onkeypress(down, "Down")
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")



while True:
    screen.update() #.update() actualiza la pantalla

    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < -300:
        time.sleep(2)
        for i in body:
            i.clear()
            i.hideturtle()
        snake.home()
        snake.direction = 'stop'
        body.clear()

        score = 0
        text.clear()
        text.write()


    if snake.distance(food) < 20: #.distance() determina la distancia hacia un objeto
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        food.goto(x,y)

        newBody = turtle.Turtle()
        newBody.shape("square")
        newBody.color("green")
        newBody.penup()
        newBody.goto(0,0)
        newBody.speed(0)
        body.append(newBody)

        score += 10
        if score > highScore:
            highScore = score
            text.clear()
            text.write("Marcador: {}\tMarcador mas alto: {}".format(score, highScore))

    total = len(body)
    for i in range(total-1,0,-1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)
    if total > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x,y)

    movement()

    for i in body:
        if i.distance(snake) < 20:
            for i in body:
                i.clear()
                i.hideturtle()
            snake.home()
            body.clear()
            snake.direction = "stop"


    time.sleep(delay)

turtle.done()