from Tkinter import *

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
    
drawSquare(c, 'red', 100, (50,50))
drawSquare(c, 'green', 100, (750,50))
drawSquare(c, 'blue', 100, (50,750))
drawSquare(c, 'yellow', 100, (750,750))

if __name__ == '__main__':  
    root.mainloop()   