from Tkinter import *
import random as r
import math as m
global root
global canvas
global color
global lineList
global N

def key_handler(event):
    '''Handle key presses. Closes the display window if 'q' is pressed, changes
    the color of the stars to a randomly selected color if 'c' is pressed, adds
    2 to the "N" value (the number of verticies on the star) if '+' is pressed,
    subtracts two from the "N" value if '-' is pressed (as long as N >= 7), and
    clears all of the stars from the canvas if 'x' is pressed.'''
    if event.keysym == 'q':
        quit()
    elif event.keysym == 'c':
        global color 
        color = random_color()
    elif event.keysym == 'plus':
        global N
        N += 2
    elif event.keysym == 'minus':
        global N
        if N >= 7:
            N -= 2
    elif event.keysym == 'x':
        global lineList
        print lineList
        for l in lineList:
            canvas.delete(l)
        lineList = []
            

def button_handler(event):
    '''Handles left mouse button click events. Draws a star of random radius in
    the range [50, 100) pixels with the color "color" at the mouse x and y 
    coordinates.'''
    draw_star(event.x, event.y, color)
        

def draw_line(start, end, color):
    '''Draws a line beginning at the (x, y) tuple "start" and ending at the
    (x, y) tuple "end", with the color "color".'''
    line1 = canvas.create_line(start[0], start[1], end[0], end[1], fill=color, \
                               width=3)  
    global lineList
    lineList.append(line1)
    return line1
    

def draw_star(x_0, y_0, col):
    '''Draws a star of random radius in the range [50, 100) pixels centered at
    (x_0, y_0) with the color col. Uses the global variable N to determine the 
    number of verticies of the star.'''
    radius = 50 + 100 * r.random()
    c1 = color
    pointList = []
    for i in range(0, N):
        theta = (-1 * m.pi / 2) + (2 * m.pi) * (float(i) / float(N))
        pointList.append((radius * m.cos(theta), radius * m.sin(theta)))
        
    for j in range(0, N):
        for k in range(0, N):
            difference = abs(j - k)
            half = (N - 1) / 2
            if difference == half or difference == (half + 1):
                (dx1, dy1) = pointList[j]
                (dx2, dy2) = pointList[k]
                x1 = x_0 + dx1
                y1 = y_0 + dy1
                x2 = x_0 + dx2
                y2 = y_0 + dy2
                draw_line((x1, y1), (x2, y2), col)
    return pointList
        
    
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
    color = random_color()
    lineList = []
    N = 5
    root.mainloop() 
    
    