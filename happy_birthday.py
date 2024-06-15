import turtle as snowflake
from turtle import *
from random import randint

kholoud = snowflake.Screen()
kholoud.bgcolor("black")
snowflake = snowflake.Turtle()
snowflake.width(7)
snowflake.shape('turtle')
snowflake.speed(29)

colors = ["orange", "red", "dark blue", "green", "#fc037f", "gold", "ivory", "red", "pink",
          "green", "blue", "light green", ]


## Main function to draw word - 'KHOLOUD'
def draw_kholoud(i, x, y):
    snowflake.pencolor("linen")
    snowflake.color(colors[i % 7])
    snowflake.begin_fill()
    snowflake.lt(70)
    snowflake.penup()
    snowflake.goto(x, y)
    snowflake.pendown()
    snowflake.circle(33)
    snowflake.end_fill()

## Code for the function call of shape - "balloon"
def ballon(x, y):
    snowflake.pensize(1)
    for i in range(5):
        draw_kholoud(i, x, y)

## Code to implement shape - 'Cake'
def cake(x, y):
    snowflake.fd(x)
    snowflake.rt(90)
    snowflake.fd(y)
    snowflake.rt(90)
    snowflake.fd(x)
    snowflake.rt(90)
    snowflake.fd(y)

## Code to implement shape - 'Heart'
def heart():
    for i in range(43):
        snowflake.pencolor(colors[i % 9])
        snowflake.rt(5)
        snowflake.fd(5)
    snowflake.pencolor("red")
    snowflake.fd(150)
    snowflake.penup()
    snowflake.rt(140)
    snowflake.fd(147)
    snowflake.pendown()
    for i in range(43):
        snowflake.pencolor(colors[i % 9])
        snowflake.lt(5)
        snowflake.fd(5)
    snowflake.pencolor("red")
    snowflake.lt(7)
    snowflake.fd(151)

## Code to implement the movement of pixels
def move(x, y):
    snowflake.up()
    snowflake.setposition(0, 0)
    snowflake.setheading(90)
    snowflake.rt(90)
    snowflake.fd(x)
    snowflake.lt(90)
    snowflake.fd(y)
    snowflake.pendown()

## Code to implement letter 'G'
def mov(x, y):
    snowflake.up()
    snowflake.setposition(0, 0)
    snowflake.setheading(90)
    snowflake.lt(90)
    snowflake.fd(x)
    snowflake.rt(90)
    snowflake.fd(y)
    snowflake.pendown()

## Code to implement letter 'G'
def A(size):
    snowflake.rt(19)
    snowflake.forward(size)
    snowflake.rt(141)
    snowflake.fd(size)
    snowflake.backward(size / 2)
    snowflake.rt(105)
    snowflake.fd(int(size / 3))

## Code to implement letter 'B'
def B(size):
    snowflake.forward(size)
    snowflake.rt(90)
    for i in range(18):
        snowflake.rt(9)
        snowflake.fd(size // 20)
    for i in range(18):
        snowflake.rt(size // 5)
        snowflake.backward(size // 20)


## Code to implement letter 'D'
def D(size):
    snowflake.fd(size)
    snowflake.rt(90)
    snowflake.fd(size // 10)
    for i in range(13):
        snowflake.rt(13)
        snowflake.fd(size // 8)

## Code to implement letter 'G'
def G(size):
        snowflake.pensize(10)
        snowflake.penup()
        snowflake.fd(size // 2)
        snowflake.pendown()
        snowflake.lt(90)
        snowflake.fd(size // 4)
        snowflake.backward(size // 1.5)
        snowflake.lt(90)
        for _ in range(size):
            snowflake.rt(4)
            snowflake.fd(4)

def S(size):
    snowflake.rt(90)
    for i in range(0,5):
        if i<3:
            snowflake.fd(size/2)
            snowflake.lt(90)
            if i==2:
                snowflake.rt(90)
        else:
            snowflake.right(90)
            snowflake.fd(size/2)

def M(size):
    snowflake.fd(int(size/2))
    snowflake.rt(135)
    snowflake.fd(int(size/3))
    snowflake.lt(90)
    snowflake.fd(int(size/3))
    snowflake.rt(135)
    snowflake.fd(int(size/2))


def H(size):
    snowflake.fd(size)
    snowflake.backward(size // 2)
    snowflake.rt(90)
    snowflake.fd(size // 2)
    snowflake.lt(90)
    snowflake.fd(size // 2)
    snowflake.backward(size)

def I(size):
    snowflake.fd(size)
    snowflake.rt(90)
    snowflake.circle(size//8)

def K(size):
    snowflake.fd(size)
    snowflake.backward(size//2)
    snowflake.rt(60)
    snowflake.fd(size//1.5)
    snowflake.backward(size//2)
    snowflake.rt(80)
    snowflake.fd(size//1.3)

def L(size):
    snowflake.fd(size)
    snowflake.backward(size)
    snowflake.rt(90)
    snowflake.fd(size // 2)


def O(size):
    for _ in range(36):
        snowflake.fd(size //13)
        snowflake.rt(10)


def P(size):
    snowflake.fd(size)
    snowflake.rt(90)
    snowflake.fd(size // 8)
    for i in range(8):
        snowflake.rt(20)
        snowflake.fd(size // 9)

def R():
    snowflake.fd(60)
    snowflake.rt(90)
    snowflake.fd(7)
    for i in range(15):
        snowflake.rt(12)
        snowflake.fd(3)
    snowflake.lt(120)
    snowflake.fd(40)

def T(size):
    snowflake.fd(size)
    snowflake.rt(90)
    snowflake.fd(size // 2)
    snowflake.backward(size // 2)

def U(size):
    snowflake.rt(90)
    for i in range(size // 10):
        snowflake.lt(15)
        snowflake.fd(size // 10)
    snowflake.fd(size // 2)
    snowflake.back(size // 2)

    for i in range(size // 10):
        snowflake.rt(13)
        snowflake.back(size // 10)
    snowflake.lt(5)
    for i in range(size // 10):
        snowflake.rt(17)
        snowflake.back(size // 10)
    snowflake.back(size // 2)


def Y(size):
    snowflake.fd(size)
    snowflake.left(60)
    snowflake.fd(size // 2)
    snowflake.backward(size // 2)
    snowflake.rt(90)
    snowflake.fd(size // 1.5)


snowflake.width(5)

ballon(223, -150)
ballon(-233, -150)

mov(20,-130)
snowflake.width(13)

heart()

## Code to implement the name section
snowflake.speed(40)
snowflake.width(4)
snowflake.pencolor("#ff3377")

snowflake.width(11)

mov(230,240)
K(60)
mov(170,240)
H(60)
mov(130,240)
O(60)
mov(70,240)
L(60)
mov(20,240)
O(60)
mov(-70,240)
U(60)
mov(-110, 240)
D(60)
mov(-170,240)
#A(60)


## Code to implement the Cake maker section
mov(120,80)
snowflake.color("#94014b")
snowflake.begin_fill()
cake(40,160)
snowflake.end_fill()
mov(110,115)
snowflake.color("#fa348a")
snowflake.begin_fill()
cake(40,140)
snowflake.end_fill()
mov(100,150)
snowflake.color("#fa78b0")
snowflake.begin_fill()
cake(40,120)
snowflake.end_fill()
mov(35,200)
snowflake.width(11)
snowflake.pencolor("red")
snowflake.circle(7)


##Code to implement the shape - "candle"

snowflake.pensize(3)
snowflake.penup()
snowflake.goto(-100,210)
snowflake.color("red")
snowflake.left(180)
snowflake.pendown()
snowflake.forward(20)

snowflake.penup()
snowflake.goto(-80,210)
snowflake.color("orange")
snowflake.pendown()
snowflake.forward(20)


snowflake.penup()
snowflake.goto(-10,210)
snowflake.color("orange")
snowflake.pendown()
snowflake.forward(20)

snowflake.penup()
snowflake.goto(20,210)
snowflake.color("red")
snowflake.pendown()
snowflake.forward(20)


## End of cake section


# #kholoud_birthday
snowflake.pencolor("#63F5F0")
snowflake.width(13)
mov(260,-30)
H(100)
snowflake.width(7)
mov(190,-30)
A(65)
mov(135,-30)
P(60)
mov(100,-30)
P(60)
mov(52,-30)
Y(60)
mov(28,-30)
B(60)
move(8,-30)
I(60)
move(36,-30)
R()
move(80,-30)
T(100)
move(102,-30)
H(60)
move(150,-30)
snowflake.pencolor("#63F5F0")
D(200)
move(160,-30)
A(60)
move(220,-30)
Y(60)
kholoud.exitonclick()

