# Dan Ryan
# Assignment 7: Tic-Tac-Toe
# Challenge
# Drawing a Tic-Tac-Toe board for fun and profit!

# make Gui3 accessible
import Gui3

# declare some constants
CANVAS_WIDTH = 350
CANVAS_HEIGHT = 350
# create the window object and set characteristics
win = Gui3.Gui()
win.title('Tic-Tac-Toe')
# make the canvas
canvas = win.ca(CANVAS_WIDTH, CANVAS_HEIGHT)


def grid():

    # make upper horizontal line
    canvas.rectangle([[-150, 50],
                     [150, 50-3]], fill='#000000')
    # make lower horizontal line
    canvas.rectangle([[-150, -50],
                     [150, -50-3]], fill='#000000')
    # make left vertical line
    canvas.rectangle([[-50, 150],
                     [-50-3, -150]], fill='#000000')
    # make right vertical line
    canvas.rectangle([[50, 150],
                     [50-3, -150]], fill='#000000')
    # and the grass
    # canvas.rectangle([[-CANVAS_WIDTH/2 + 2, -CANVAS_HEIGHT/2],
    #                  [CANVAS_WIDTH/2, 0]], fill='#009900')
    #
    # upTriangle(-100, -50, 120, 30, '#993300', canvas)


# define a helper function to draw a triangle
def upTriangle(x, y, w, h, color, canvas):
    canvas.polygon([[x, y], [x + w, y], [x + w/2, y + h]],
                   fill=color, outline='black')


# call main, which creates the Tic-Tac-Toe grid/board
grid()

# invoke tkinter: displays objects drawn!
win.mainloop()
