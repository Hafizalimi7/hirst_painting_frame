from turtle import Turtle, Screen
import random

color_list = [(40, 98, 148), (178, 46, 78), (205, 160, 93), (224, 210, 102), (137, 89, 63), (178, 165, 36), (110, 175, 208), (213, 130, 174), (228, 72, 48), (201, 74, 117), (92, 103, 188), (22, 154, 87), (122, 217, 208), (126, 41, 70), (95, 158, 62), (45, 190, 204), (226, 171, 187), (130, 189, 161), (213, 206, 38), (232, 171, 163), (172, 186, 222), (153, 208, 218), (104, 50, 38), (45, 62, 101), (44, 75, 80), (51, 61, 71)]

screen = Screen()
screen.colormode(255)
tim = Turtle()

def set_up():
    tim.speed("fastest")
    tim.hideturtle()
    tim.setheading(225)
    tim.penup()
    tim.forward(300)
    tim.setheading(0)


set_up()

num_of_dot = 100
for dot_count in range(1, num_of_dot+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()