# Pull in Gui3 so we can use it...
import Gui3


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


def showWindow(title):
    # define win as the gui subcomponent of gui3
    win = Gui3.Gui()
    win.title(title)
    win.mainloop()


# Main funtion, where the magic happens!
def main():
    stuff = userInput()
    showWindow('First Window')
    showWindow('Second Window')

    # Set the variable that controls canv
    width = int(stuff['width'])
    height = int(stuff['height'])

    canvas = win.ca(width + 50, height + 50)

    canvas.rectangle([[-width/2, -height/2], [width/2, height/2]], fill='yellow')

    canvas.oval([[-width/2, -height/2], [width/2, height/2]], fill='#00ff00')

    canvas.polygon([[-width/2, 0], [0, height/2], [width/2, 0], [0, -height/2]],
                   outline='black', fill='white')

    win.mainloop()


# Lets run our main function!
main()
