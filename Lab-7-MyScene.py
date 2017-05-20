# Dan Ryan
# Lab 7: MyScene
# Plus
# Make a nice little environment to look at, with grass, sky, trees & houses!

# make Gui3 accessible
import Gui3

# declare some constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
# create the window object and set characteristics
win = Gui3.Gui()
win.title('My Scene')
# make the canvas
canvas = win.ca(CANVAS_WIDTH, CANVAS_HEIGHT)


# the main function
def main():

    # make the sky
    canvas.rectangle([[-CANVAS_WIDTH/2 + 2, -CANVAS_HEIGHT/2],
                     [CANVAS_WIDTH/2, CANVAS_HEIGHT/2 - 2]], fill='#00ccff')
    # and the grass
    canvas.rectangle([[-CANVAS_WIDTH/2 + 2, -CANVAS_HEIGHT/2],
                     [CANVAS_WIDTH/2, 0]], fill='#009900')

    upTriangle(-100, -50, 120, 30, '#993300', canvas)


# define a helper function to draw a triangle
def upTriangle(x, y, w, h, color, canvas):
    canvas.polygon([[x, y], [x + w, y], [x + w/2, y + h]],
                   fill=color, outline='black')


# call main, which prints the sky & grass
main()


# Here we print triangular trees
def tree(x, y, canvas, color='#006600'):
    # draw the tree, first the top
    upTriangle(x, y, 50, 100, color, canvas)
    # then the trunk
    canvas.rectangle([[x+21, y-20], [x+29, y]], fill='brown')


# This prints oval trees, woo!
def lolipop(x, y, canvas, color='#006600'):
    # draw the tree, first the top
    canvas.oval([[x+50, y], [x, y+90]], fill=color)
    # then the trunk
    canvas.rectangle([[x+21, y-20], [x+29, y]], fill='brown')


# Lets print some trees
tree(100, -40, canvas, '#aaaa00')
tree(60, -60, canvas)
tree(0, -140, canvas, '#aa0000')
# Now to print the oval trees :P
lolipop(-20, -15, canvas, '#aaaa00')
lolipop(140, -15, canvas)


# Created house function
def house(x, y, canvas, color='blue'):
    canvas.rectangle([[x+10, y], [x+110, y+50]], fill=color)
    canvas.rectangle([[x+48, y], [x+72, y+40]], fill='#996633')
    upTriangle(x, y+50, 120, 30, '#993300', canvas)


# Pink house
house(-180, -32, canvas, '#FFC0CB')
# Normal house
house(-100, -100, canvas)
# Green house
house(70, -130, canvas, '#006400')

# invoke tkinter: displays objects drawn!
win.mainloop()
