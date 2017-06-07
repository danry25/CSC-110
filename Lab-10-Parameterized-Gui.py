# Pull in Gui3 so we can use it...
import Gui3
# define win as the gui subcomponent of gui3


def userInput():
    stuff = {'corners': '4', 'height': '200', 'title': 'fun', 'width': '200'}
    # stuff = {
    #     "title": input('Enter a title: '),
    #     "width": input('Width for the rectangle: '),
    #     "height": input('Height for the rectangle: '),
    #     "corners": input('Enter the number of corners for the plus: ')
    # }
    # print(stuff)
    return stuff


def showWindow(stuff, type):
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
    else:
        # Create window on user's screen
        win = Gui3.Gui()
        # Title the Window
        win.title('Second Window')
        # Set the variable that controls canvas & inner shape size
        width = 250
        height = 250
        # Create canvas
        canvas = win.ca(width + 50, height + 50)
        # Draw shapes
        canvas.rectangle([[-width/2, -height/2], [width/2, height/2]], fill='yellow')
        canvas.oval([[-width/2, -height/2], [width/2, height/2]], fill='#00ff00')
        canvas.polygon([[-width/2, 0], [0, height/2], [width/2, 0], [0, -height/2]],
                       outline='black', fill='white')
        # Show the canvas to the user
        win.mainloop()


# Main funtion, where the magic happens!
def main():
    # Get user input
    stuff = userInput()
    showWindow(stuff, True)
    showWindow(stuff, False)


# Lets run our main function!
main()
