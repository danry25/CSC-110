# Dan Ryan
# Lab 10: Parameterized Gui
# Plus
# Draw shapes on the screen, of different sizes and shapes depending on user input

# Pull in Gui3 so we can use it...
import Gui3
import math
# define win as the gui subcomponent of gui3


# Handles gathering and checking user input
def userInput():
    # Gather the actual user input and store it
    stuff = {
        "title": input('Enter a title: '),
        "width": input('Width for the rectangle: '),
        "height": input('Height for the rectangle: '),
        "corners": input('Enter the number of corners for the plus: ')
    }
    # Authenticate user input so as to avoid program crashes
    while stuff['title'] == '':
        # user input error triggered
        print('Error in input. Title cannot be blank.')
        stuff['title'] = input('Try again. Enter a title: ')
    while not stuff['width'].isdigit():
        # user input error triggered
        print('Error in input. Width cannot be blank or non-numeric.')
        stuff['width'] = input('Try again. Enter the width: ')
    while not stuff['height'].isdigit():
        # user input error triggered
        print('Error in input. height cannot be blank or non-numeric.')
        stuff['height'] = input('Try again. Enter the height: ')
    while not stuff['corners'].isdigit():
        # user input error triggered
        print('Error in input. Corners cannot be blank or non-numeric.')
        stuff['width'] = input('Try again. Enter the Corners: ')
    return stuff


# Creates 2 different types of windows, dependent on input
def showWindow(stuff, type):
    # Window 1 is created if type is true
    if type:
        # Create window on user's screen
        win = Gui3.Gui()
        # Title the Window
        win.title(stuff['title'])
        # Set the variable that controls canvas & inner shape size
        width = int(stuff['width'])
        height = int(stuff['height'])
        # Create canvas
        canvas = win.ca(width + 50, height + 50)
        # Draw shapes
        canvas.rectangle([[-width/2, -height/2], [width/2, height/2]], fill='yellow')
        canvas.oval([[-width/2, -height/2], [width/2, height/2]], fill='#00ff00')
        canvas.polygon([[-width/2, 0], [0, height/2], [width/2, 0], [0, -height/2]],
                       outline='black', fill='white')
        # Show the canvas to the user
        win.mainloop()
    # If type is false, Window 2 gets created
    else:
        # Create window on user's screen
        win = Gui3.Gui()
        # Title the Window
        win.title('Second Window')
        # Set the variable that controls inner shape size
        width = 200
        height = 200
        # Create a variable that rachets up each loop, for use inside equation
        step = 0
        # Make a place to store these beautiful coordinates
        coords = []
        for corner in range(int(stuff['corners'])):
            r = 100
            O = math.pi/2 + (step * (2*math.pi)/int(stuff['corners']))
            coords.append([int(r * math.cos(O)), int(r * math.sin(O))])
            step += 1
        # Create canvas
        canvas = win.ca(250, 250)
        # Draw shapes
        canvas.rectangle([[-width/2, -height/2], [width/2, height/2]], fill='yellow')
        canvas.oval([[-width/2, -height/2], [width/2, height/2]], fill='#00ff00')
        # Make a polygon with the aformentioned coordinates
        canvas.polygon(coords, outline='black', fill='white')
        # Show the canvas to the user
        win.mainloop()


# Main funtion, where the magic happens!
def main():
    # Get user input
    stuff = userInput()
    # Create window 1
    showWindow(stuff, True)
    # Make window 2
    showWindow(stuff, False)


# Lets run our main function!
main()
