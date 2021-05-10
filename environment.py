from tkinter import *

root = Tk()
WIDTH = 900
HEIGHT = 600

# create the canvas which is a black background
canvas = Canvas(root, bg='black', width=900, height=600)

# create the paddle for the game
paddle = canvas.create_rectangle(75, 100, 300, 75, fill='gray60')

# Ball class
class Ball:
    # constructor
    def __init__(self):
        self.shape = canvas.create_oval(0, 0, 50, 50, fill='white')
        self.speedx = 11 # changed from 3 to 9
        self.speedy = 11 # changed from 3 to 9
        self.active = True
        self.move_active()

    # ball update method
    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        # if the xpos exceeds 900 or is less than 0, the ball will 'bounce'
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        # if the ypos exceeds 600 or is less than 0, the ball will 'bounce'
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

    # move active method
    def move_active(self):
        if self.active:
            self.ball_update()
            root.after(40, self.move_active) # changed from 10ms to 30ms


# create a ball object
ball = Ball()

# set the position of the paddle
canvas.move(paddle, 250, 500)

# set up the bricks
# each brick will be rectangle
# there will be 28 bricks
# setting up the red bricks

brick1 = canvas.create_rectangle(75, 50, 175, 75, fill='red')
brick2 = canvas.create_rectangle(75, 50, 175, 75, fill='red')
canvas.move(brick2, 100, 0)
brick3 = canvas.create_rectangle(75, 50, 175, 75, fill='red')
canvas.move(brick3, 200, 0)
brick4 = canvas.create_rectangle(75, 50, 175, 75, fill='red')
canvas.move(brick4, 300, 0)
brick5 = canvas.create_rectangle(75, 50, 175, 75, fill='red')
canvas.move(brick5, 400, 0)
brick6 = canvas.create_rectangle(75, 50, 175, 75, fill='red')
canvas.move(brick6, 500, 0)
brick7 = canvas.create_rectangle(75, 50, 175, 75, fill='red')
canvas.move(brick7, 600, 0)
# setting up the green bricks
brick8 = canvas.create_rectangle(75, 50, 175, 75, fill='green')
canvas.move(brick8, 0, 25)
brick9 = canvas.create_rectangle(75, 50, 175, 75, fill='green')
canvas.move(brick9, 100, 25)
brick10 = canvas.create_rectangle(75, 50, 175, 75, fill='green')
canvas.move(brick10, 200, 25)
brick11 = canvas.create_rectangle(75, 50, 175, 75, fill='green')
canvas.move(brick11, 300, 25)
brick12 = canvas.create_rectangle(75, 50, 175, 75, fill='green')
canvas.move(brick12, 400, 25)
brick13 = canvas.create_rectangle(75, 50, 175, 75, fill='green')
canvas.move(brick13, 500, 25)
brick14 = canvas.create_rectangle(75, 50, 175, 75, fill='green')
canvas.move(brick14, 600, 25)
# setting up the yellow bricks
brick15 = canvas.create_rectangle(75, 50, 175, 75, fill='yellow')
canvas.move(brick15, 0, 50)
brick16 = canvas.create_rectangle(75, 50, 175, 75, fill='yellow')
canvas.move(brick16, 100, 50)
brick17 = canvas.create_rectangle(75, 50, 175, 75, fill='yellow')
canvas.move(brick17, 200, 50)
brick18 = canvas.create_rectangle(75, 50, 175, 75, fill='yellow')
canvas.move(brick18, 300, 50)
brick19 = canvas.create_rectangle(75, 50, 175, 75, fill='yellow')
canvas.move(brick19, 400, 50)
brick20 = canvas.create_rectangle(75, 50, 175, 75, fill='yellow')
canvas.move(brick20, 500, 50)
brick21 = canvas.create_rectangle(75, 50, 175, 75, fill='yellow')
canvas.move(brick21, 600, 50)
# setting up the purple bricks
brick22 = canvas.create_rectangle(75, 50, 175, 75, fill='royal blue')
canvas.move(brick22, 0, 75)
brick23 = canvas.create_rectangle(75, 50, 175, 75, fill='royal blue')
canvas.move(brick23, 100, 75)
brick24 = canvas.create_rectangle(75, 50, 175, 75, fill='royal blue')
canvas.move(brick24, 200, 75)
brick25 = canvas.create_rectangle(75, 50, 175, 75, fill='royal blue')
canvas.move(brick25, 300, 75)
brick26 = canvas.create_rectangle(75, 50, 175, 75, fill='royal blue')
canvas.move(brick26, 400, 75)
brick27 = canvas.create_rectangle(75, 50, 175, 75, fill='royal blue')
canvas.move(brick27, 500, 75)
brick28 = canvas.create_rectangle(75, 50, 175, 75, fill='royal blue')
canvas.move(brick28, 600, 75)

canvas.pack(expand=True, fill=BOTH)


# function to move paddle left
def left(event):
    x = -15
    y = 0
    canvas.move(paddle, x, y)


# function to move paddle right
def right(event):
    x = 15
    y = 0
    canvas.move(paddle, x, y)

# bind the events to root
root.bind("<Left>", left)
root.bind("<Right>", right)

root.mainloop()