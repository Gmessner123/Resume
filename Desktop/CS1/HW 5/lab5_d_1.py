from Tkinter import *
import random as r
global root
global canvas
global color
global eventList

def key_handler(event):
    '''Handles key presses. Closes the display window if 'q' is pressed, changes
    the color of the circles to a randomly selected color if 'c' is pressed, and
    clears all of the circles from the canvas if 'x' is pressed.'''
    if event.keysym == 'q':
        quit()
    elif event.keysym == 'c':
        global color 
        color = random_color()
    elif event.keysym == 'x':
        global eventList
        for ev in eventList:
            canvas.delete(ev)
        eventList = []
            

def button_handler(event):
    '''Handles left mouse button click events. Draws an oval of random radius in
    the range [10, 50) pixels with the color "color".'''
    radius = 10 + 40 * r.random()
    oval = canvas.create_oval(event.x - radius, event.y - radius, event.x + \
                              radius, event.y + radius, outline=color, \
                              fill=color, width=4)    
    global eventList
    eventList.append(oval)
    
        
def random_color():
    '''Returns a string representing a random color supported by the Tkinter 
    package.'''
    chars = '0123456789abcdef'
    s = '#'
    for i in range(0, 6):
        s += r.choice(chars)
    return s  


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)
    eventList = []
    color = random_color()
    root.mainloop()    
