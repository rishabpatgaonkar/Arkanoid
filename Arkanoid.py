__author__ = "Rishab Patgaonkar"
__copyright__ = "Copyright (C) 2021 Rishab Patgaonkar"
__license__ = "Public Domain"
__version__ = "1.0"

from tkinter import *
from tkinter import messagebox

root = Tk()
WIDTH = 900
HEIGHT = 600
# create the canvas which is a black background
canvas = Canvas(root, bg='black', width=900, height=600)

# create the paddle for the game
paddle = canvas.create_rectangle(75, 100, 150, 75, fill='gray60')

# set up the bricks
# each brick will be rectangle
# there will be 28 bricks
# setting up the red bricks
redBricks = []
for i in range(7):
    x = (i*100) + 75
    y = 50
    redBrick = canvas.create_rectangle(x, y, x+100, 75, fill="red")
    redBricks.append(redBrick)

# setting up the green bricks
greenBricks = []
for i in range(7):
    x = (i*100) + 75
    y = 75
    greenBrick = canvas.create_rectangle(x, y, x+100, 100, fill="green")
    greenBricks.append(greenBrick)

# setting up the yellow bricks
yellowBricks = []
for i in range(7):
    x = (i*100) + 75
    y = 100
    yellowBrick = canvas.create_rectangle(x, y, x+100, 125, fill="yellow")
    yellowBricks.append(yellowBrick)

# setting up the blue bricks
blueBricks = []
for i in range(7):
    x = (i*100) + 75
    y = 125
    blueBrick = canvas.create_rectangle(x, y, x+100, 150, fill="royal blue")
    blueBricks.append(blueBrick)


# Ball class
class Ball:

    # constructor
    def __init__(self):
        self.score = 0
        self.shape = canvas.create_oval(15, 15, 30, 30, fill='white')
        canvas.move(self.shape, 250, 500)
        self.speedx = 10  # changed from 3 to 9
        self.speedy = 10  # changed from 3 to 9
        self.active = True
        self.move_active()

    # ball update method
    def ball_update(self):

        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        # collide checks to see if the pos of the ball is overlapping another shape
        collide = canvas.find_overlapping(*pos)
        # if the xpos exceeds 900 or is less than 0, the ball will 'bounce'
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        # if the ypos exceeds 600 or is less than 0, the ball will 'bounce'
        if pos[1] <= 0:
            self.speedy *= -1
        # check if the ball has went out of bounds
        if pos[3] > HEIGHT:
            messagebox.showwarning("Game Over!", "Game Over!\nYour Final Score: %d" % self.score)
            print('Game Over!')
            root.destroy()
            # canvas.delete('all')
        # check if the ball collides with the paddle
        if paddle in collide:
            self.speedy *= -1
        # check to see if the ball collides with a blue brick
        for blueBrick in blueBricks:
            if blueBrick in collide:
                blueBricks.remove(blueBrick)
                canvas.delete(blueBrick)
                # global score
                self.score += 1
                # causes the ball to bounce back
                self.speedy *= -1
        # check to see if the ball collides with a red brick
        for redBrick in redBricks:
            if redBrick in collide:
                redBricks.remove(redBrick)
                canvas.delete(redBrick)
                # global score
                self.score += 1
                # causes the ball to bounce back
                self.speedy *= -1
        # check to see if the ball collides with a yellow brick
        for yellowBrick in yellowBricks:
            if yellowBrick in collide:
                yellowBricks.remove(yellowBrick)
                canvas.delete(yellowBrick)
                # global score
                self.score += 1
                self.speedy *= -1
        # check to see if the ball collides with a blue brick
        for greenBrick in greenBricks:
            if greenBrick in collide:
                greenBricks.remove(greenBrick)
                canvas.delete(greenBrick)
                # global score
                self.score += 1
                self.speedy *= -1

    # move active method
    def move_active(self):
        if self.active:
            self.ball_update()
            root.after(40, self.move_active)  # changed from 10ms to 30ms


# create a ball object
ball = Ball()

# set the position of the paddle
canvas.move(paddle, 250, 500)

canvas.pack(expand=True, fill=BOTH)


# function to move paddle left
def left(event):
    x = -10
    y = 0
    canvas.move(paddle, x, y)


# function to move paddle right
def right(event):
    x = 10
    y = 0
    canvas.move(paddle, x, y)


# bind the events to root
root.bind("<Left>", left)
root.bind("<Right>", right)

root.mainloop()
