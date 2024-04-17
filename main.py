import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter the color.")
colors = ["purple", "orange", "red", "green", "blue", "yellow"]
all_turtles = []


if user_bet:
    is_race_on = True
i = 0
a = 100
for _ in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[int(i)])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-a)
    all_turtles.append(new_turtle)
    a -= 30
    i += 1
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
