from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)



class Snake:

    # crea una lista contenente tutte le parti del serpente
    snake_element = []
    
    # definisce le coordinate iniziali del serpente
    def __init__(self):
        
        STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

        for index in STARTING_POSITION:
            self.spawn_snake(index)

    # crea l'oggetto e lo aggiunge alla lista
    def spawn_snake(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)

        self.snake_element.append(snake_segment)
        screen.update()

    # aggiunge un elemento alla coda quando il serpente mangia
    def add_segment(self):
        self.spawn_snake(self.snake_element[-1].position())

    def move(self):

        # sposta gli elementi secondo la direzione del serpente
        for index in range(len(self.snake_element)-1, 0, -1):
            x = self.snake_element[index - 1].xcor()
            y = self.snake_element[index - 1].ycor()
            self.snake_element[index].goto(x, y)

        # muove la testa avanti di 20
        self.snake_element[0].forward(20)
        screen.update()
        time.sleep(0.1)

    # muove il serpente secondo la direzione indicata
    def DirectionMove(self, value):
        for index in range(0, len(self.snake_element)):
            x = self.snake_element[index - 1].xcor()
            y = self.snake_element[index - 1].ycor()
            self.snake_element[index].setheading(value)

    # assegna la direzione da seguire
    #   se viene premuto il tasto direzione opposto alla direzione corrente
    #   il tasto non cambierà la direzione
    def move_up(self):
        if self.snake_element[0].heading() == 270: return
        Snake.DirectionMove(self, 90)

    def move_down(self):
        if self.snake_element[0].heading() == 90: return
        Snake.DirectionMove(self, 270)

    def move_left(self):
        if self.snake_element[0].heading() == 0: return
        Snake.DirectionMove(self, 180)

    def move_right(self):
        if self.snake_element[0].heading() == 180: return
        Snake.DirectionMove(self, 0)



class Food(Turtle):
    
    def __init__(self):

        # crea il cibo del serpente
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed(0)
        self.refresh()

    # assegna delle coordinate casuali al cibo
    def refresh(self):
        rand_x = random.randint(-14, 14)*20
        rand_y = random.randint(-14, 14)*20
        self.goto(rand_x, rand_y)



class Scoreboard(Turtle):

    def __init__(self):
        
        # crea la scoreboard
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = -1
        self.refresh_score()
        
    # aggiunge +1 alla scoreboard
    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", font=('Courier', 17,'bold'))

    # stampa GAME OVER a schermo
    def game_over(self):
        self.home()
        self.write("GAME OVER", False, "center", font=('Courier', 17,'bold'))