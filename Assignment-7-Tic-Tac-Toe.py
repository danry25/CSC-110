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

# Assign each square a number
LOWER_LEFT = 0
LOWER_MIDDLE = 1
LOWER_RIGHT = 2
MID_LEFT = 3
CENTER = 4
MID_RIGHT = 5
UPPER_LEFT = 6
UPPER_MIDDLE = 7
UPPER_RIGHT = 8

# Store square's x & y coordinate values
squareX = [-150, 49, 150, -150, 49, 150, -150, 50, 150]
squareY = [-150, -150, -150, 49, 49, 49, 150, 150, 150]


def board(x, y, canvas):

    # make upper horizontal line
    canvas.rectangle([[-150, 52],
                     [150, 52-3]], fill='#000000')
    # make lower horizontal line
    canvas.rectangle([[-150, -49],
                     [150, -49-3]], fill='#000000')
    # make left vertical line
    canvas.rectangle([[-49, 150],
                     [-49-3, -150]], fill='#000000')
    # make right vertical line
    canvas.rectangle([[52, 150],
                     [52-3, -150]], fill='#000000')
    # and the grass
    # canvas.rectangle([[-CANVAS_WIDTH/2 + 2, -CANVAS_HEIGHT/2],
    #                  [CANVAS_WIDTH/2, 0]], fill='#009900')
    #
    # upTriangle(-100, -50, 120, 30, '#993300', canvas)


# helper function to draw X
def drawX(position, canvas):
    x = squareX[position] + 10
    y = squareY[position] + 10
    canvas.line([[x, y], [x + 80, y + 80]], width=7)
    canvas.line([[x + 80, y], [x, y + 80]], width=7)
    # canvas.line([[-140, -140], [-60, -60]], width=7)
    # canvas.line([[-60, -140], [-140, -60]], width=7)


# helper function to draw O
def drawO(position, canvas):
    x = squareX[position] + 49
    y = squareY[position] - 51
    # squares[positions.index(position)]
    canvas.circle([x, y], 40, width=7)
    pass


# define a helper function to draw a triangle
def upTriangle(x, y, w, h, color, canvas):
    canvas.polygon([[x, y], [x + w, y], [x + w/2, y + h]],
                   fill=color, outline='black')


# call main, which creates the Tic-Tac-Toe grid/board
board(-150, -150, canvas)
drawX(LOWER_LEFT, canvas)
drawO(UPPER_LEFT, canvas)
# drawO(UPPER_MIDDLE, canvas)
# drawO(CENTER, canvas)
# drawO(MID_LEFT, canvas)
# drawO(LOWER_LEFT, canvas)
# invoke tkinter: displays objects drawn!
win.mainloop()
