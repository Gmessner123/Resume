'''
lab3d.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

#Plant
plant = { 'start' : 'X', 
          'X'     : 'F-[[X]+X]+F[+FX]-X', 
          'F'     : 'FF' }

plant_draw = { 'F' : 'F 1', 
               '-' : 'L 25', 
               '+' : 'R 25' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 

def update(lsys, s):
    '''<docstring>'''
    for key in lsys:   
        s1 = s.replace(key, lsys[key]) 
    return s1

def iterate(lsys, n):
    '''<docstring>'''
    s=lsys['start']
    for i in range(0, n):
        s = update(lsys,s)
    return s

def lsystemToDrawingCommands(draw, s):
    '''<docstring>'''
    l=[]
    for c in s:
        if c in draw:
            l.append(draw[c])
    return l

def nextLocation(x, y, angle, cmd):
    '''<docstring>'''
    l = cmd.split()
    if l[0] == 'L':
        angle += float(l[1])
        angle %= 360
    elif l[0] == 'R':
        angle -= float(l[1])
        angle %= 360
    elif l[0] == 'F':
        angle2 = angle * (math.pi / 180)
        x += float(l[1]) * math.cos(float(angle2))
        y += float(l[1]) * math.sin(float(angle2))      
    return (x, y, angle)

def bounds(cmds):
    '''<docstring>'''
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    xnow = 0
    ynow = 0
    thetanow=0
    for e in cmds:
        (xnow, ynow, thetanow) = nextLocation(xnow, ynow, thetanow, e)
        if(xnow > xmax):
            xmax = xnow
        if(xnow < xmin):
            xmin = xnow
        if(ynow > ymax):
            ymax = ynow
        if(ynow < ymin):
            ymin = ynow
        
    return (xmin, xmax, ymin, ymax)

def saveDrawing(filename, bounds, cmds):
    '''<docstring>'''
    f = open(filename, 'w')
    line = f.write(bounds[0] + ' '+ bounds[1] + ' '+ bounds[2] + ' '+ bounds[3])
    line = f.write('\n')
    
    for i in range(0, len(cmds)):
        line = f.write(cmds[i])
        line = f.write('\n')
        
    f.close()

def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print 'Making drawings for %s...' % name
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)

