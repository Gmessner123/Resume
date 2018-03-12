from Tkinter import *
import random as r

root = Tk()
c = Canvas(root, width=800, height=800)
c.pack() 
root.geometry('800x800')

def drawSquare(can, color, length, pos):
    '''Draws a square with side length length and color color on the canvas
    can. Square is centered at position pos.'''
    x = pos[0]
    y = pos[1]
   
    r = can.create_rectangle(x-length/2, y-length/2, x+length/2, y+length/2, 
    fill=color, outline=color)
    
def random_size(int1, int2):
    '''Returns a random even integer in the range [int1, int2]. Checks to make
    sure that int1, int2 are non-negative, even integers, with int1 > int2, and
    that the output integer is even as well.'''
    half1 = int1 / 2
    half2 = int2 / 2
    rand = r.randint(half1, half2)
    
    assert int1 >= 0
    assert int2 >= 0
    assert int1 % 2 == 0
    assert int2 % 2 == 0
    assert int1 < int2
    assert (rand * 2) % 2 == 0

    return rand * 2

def random_position(max_x, max_y):
    '''Returns an (x, y) tuple representing random (x, y) coordinates in the 
    ranges 0 <= x <= max_x and 0 <= y <= max_y. Also checks to make sure that
    max_x and max_y are both non-negative.'''
    randX = r.randint(0, max_x)
    randY = r.randint(0, max_y)
    
    assert max_x >= 0
    assert max_y >= 0 
    
    return (randX, randY)
    

def random_color():
    '''Returns a string representing a random color supported by the Tkinter 
    package.'''
    chars = '0123456789abcdef'
    s = '#'
    for i in range(0, 6):
        s += r.choice(chars)
    return s

def draw_random_squares(num):
    '''Generates num number of squares of random color, size, and position, and
    displays them on the canvas. The sizes range from 20-150 pixels, and the
    positions range anywhere from (0,0) to (800, 800).'''
    for i in range(0, num):
        color = random_color()
        size = random_size(20, 150)
        position = random_position(800, 800)
        drawSquare(c, color, size, position)

draw_random_squares(50)
        
def quitPython(event):
    '''Quits out of the display window when the 'q' key is pressed.'''
    quit()
    
if __name__ == '__main__': 
    root.bind('<q>', quitPython)
    root.mainloop()