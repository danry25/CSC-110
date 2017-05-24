# Dan Ryan
# Assignment 7: Tic-Tac-Toe
# Standard
# Drawing a Tic-Tac-Toe board for fun and profit!

# make Gui3 accessible
import Gui3

# declare some constants
CANVAS_WIDTH = 690
CANVAS_HEIGHT = 360
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

# # Make board size a global variable
# size = 0
# x = -150
# y = -150


def board(x, y, canvas, size=300):
    size = size
    half = size/2
    six = size/6
    y = half + six + y - 50
    x = half + six + x - 50
    if size <= 50:
        linewidth = 1
    else:
        linewidth = 3
    # make upper horizontal line
    canvas.rectangle([[-half + x, six + y],
                     [half + x, six + y - linewidth]], fill='#000000')
    # make lower horizontal line
    canvas.rectangle([[-half + x, -six + y],
                     [half + x, -six + y - linewidth]], fill='#000000')
    # make left vertical line
    canvas.rectangle([[-six + x, half + y],
                     [-six + x - linewidth, -half + y]], fill='#000000')
    # make right vertical line
    canvas.rectangle([[six + x, half + y],
                     [six + x - linewidth, -half + y]], fill='#000000')


# helper function to draw X
def drawX(x, y, canvas):
    # x = squareX[position] + 10
    # y = squareY[position] + 10
    x = x + 10
    y = y + 10
    canvas.line([[x, y], [x + 80, y + 80]], width=7)
    canvas.line([[x + 80, y], [x, y + 80]], width=7)
    # canvas.line([[-140, -140], [-60, -60]], width=7)
    # canvas.line([[-60, -140], [-140, -60]], width=7)


# helper function to draw O
def drawO(x, y, canvas):
    # x = squareX[position] + 49
    # y = squareY[position] - 51
    x = x + 49
    y = y - 51
    # squares[positions.index(position)]
    canvas.circle([x, y], 40, width=7)
    pass


# Partially done attempt at challenge work
# board(-150, -150, canvas, 50)
# drawX(LOWER_LEFT, canvas)
# drawO(UPPER_LEFT, canvas)

# 1st Board
board(-315, -150, canvas)
drawX(-315, -150, canvas)
drawO(-215, -50, canvas)
drawX(-215, 50, canvas)
drawO(-215, 50, canvas)
# 2nd Board
board(15, -150, canvas)
drawX(15, -150, canvas)
drawO(115, -50, canvas)
drawX(115, 50, canvas)
drawO(115, 50, canvas)
# call main, which creates the Tic-Tac-Toe grid/board
win.mainloop()
