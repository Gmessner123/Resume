import random as r
from Tkinter import *

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

def count_values(d):
    '''Counts the number of distinct (non-repeated) values in the input 
    dictionary d.'''
    occurred = []
    count = 0
    
    for val in d.values():
        if val in occurred:
            count += 0
        else:
            count += 1
            occurred.append(val)
            
    return count
        
def remove_value(d, item):
    '''Removes all key/ value occurrances of the potential value item in the 
    dictionary d.'''
    removeLater = []
    for key in d.keys():
        if d[key] == item:
            removeLater.append(key)
        
    for e in removeLater:
        del d[e]
        
def split_dict(d):
    '''Splits the dictionary d into a tuple of two dictionaries, one of which 
    has keys that start with letters a-m, and another with keys starting with
    n-z. Returns the tuple.'''
    d1 = {}
    d2 = {}
    
    for key in d.keys():
        key1 = key.lower()
        if key1 < 'n':
            d1[key] = d[key]
        else:
            d2[key] = d[key]
    
    return (d1, d2)

def count_duplicates(d):
    '''Returns the number of duplicate values that appear in the given 
    dictionary d. Duplicate values are values that appear at least twice.'''
    occurred = []
    occurredTwice = []
    count = 0
        
    for val in d.values():
        if val in occurred:
            if val in occurredTwice:
                count += 0
            else:
                count += 1
                occurredTwice.append(val)
        else:
            occurred.append(val)
            
    return count
            

