# 5.B.1:

import math as m

class Point:
    '''Represents a three-dimensional point with x, y, and z coordinates.'''
    
    def __init__(self, x, y, z):
        '''Constructor for objects of class Point. Stores the values x, y and
        z in the class.'''
        self.x = x
        self.y = y
        self.z = z
        
    def distanceTo(self, p):
        '''Computes the distance between the "self" point and the parameter
        point p.'''
        return m.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2 + \
                      (self.z - p.z) ** 2)


# 5.B.2:

class Triangle:
    '''Represents a triangle defined by points p1, p2, and p3 as verticies.'''
    
    def __init__(self, p1, p2, p3):
        '''Constructor for objects of class Triangle. Stores the values of p1,
        p2, and p3 in the class.'''
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def area(self):
        '''Computes the area of the triangle defined in the class by using 
        Heron's formula for area..'''
        a = self.p1.distanceTo(self.p2)
        b = self.p2.distanceTo(self.p3)
        c = self.p3.distanceTo(self.p1)
        s = (a + b + c) / 2
        return m.sqrt(s * (s - a) * (s - b) * (s - c))

#5.B.3:

class Averager:
    '''An upgraded version of the Python "list" class that keeps track of its
    length, sum, average, and min/max values.'''
    
    def __init__(self):
        '''Initializes objects of class "Averager" and sets up the main list 
        (nums) to be empty, and the number of elements (n) and sum (total) to be
        zero.'''
        self.nums = []
        self.total = 0.0
        self.n = 0.0
    
    def getNums(self):
        '''Returns a copy of the main list used in the object (nums).'''
        return self.nums[:]
    
    def append(self, num):
        '''Adds an element to the end of the main list nums, updating the sum of
        the elements and the number of elements.'''
        self.nums.append(num)
        self.total += num
        self.n += 1
    
    def extend(self, l):
        '''Adds the entire list l to the end of the main list nums. Uses the 
        append method defined above to add each element while updating the sum
        and number of elements.'''
        for i in l:
            self.append(i)
    
    def average(self):
        '''Returns the average of the elements in the main list nums. Returns
        0 if the list is empty.'''
        if self.n != 0.0:
            return float(self.total) / float(self.n)
        else:
            return 0.0
        
    
    def limits(self):
        '''Returns the lowest and highest values in the main list nums.'''
        if self.n == 0.0:
            return (0.0, 0.0)
        low = self.nums[0]
        high = self.nums[0]
        for k in self.nums:
            if k < low:
                low = k
            elif k > high:
                high = k
        
        return (low, high)

a = Averager()
print a.average()
print a.total
print a.limits()

# 5.C.1: This code is slightly inefficient in determining whether or not x is
# positive. Rather than using an "if...else..." to check different cases of x,
# the code could simply write "return x > 0" to determine whether or not x is 
# positive more quickly and efficiently (shown below).

def is_positive(x):
    '''Test if x is positive.'''
    return x > 0

# 5.C.2: Rather than assigning a boolean value (found) be false at the beginning
# of the loop, then changing it to be true if the value is found and then using
# an "if...else..." to determine whether to return an index or the value of -1 
# (i.e., the value is not in the list), the code could simply return the value
# immeditately once it is found, or return -1 if the "for" loop terminates 
# without the value being found (shown below).

def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    for i, item in enumerate(lst):
        if item == x:
            return i
    return -1

# 5.C.3: There are two design flaws in this code. (1) This code doesn't need to
# create a variable "category" and return it. Instead, it could simply return 
# directly the category that the value of x corresponds to (i.e., "return 
# 'negative'" if x is less than 0). Also, the code should use elif and else 
# statements, rather than just if statements, to make sure that not every 
# condition needs to be checked if the value of x is already clearly negative
# (shown below).

def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''
    if x < 0:
        return 'negative'
    elif x == 0:
        return 'zero'
    elif x > 0 and x < 10:
        return 'small'
    else:
        return 'large'
    
# 5.C.4: The first "if" statement and first two "elif" statements in this code
# are essentially useless. Because the code for the final "elif" statement 
# returns the correct output for the first three cases (the list length == 0, 1,
# and 2), they don't need to be there at all. Thus, we can just remove this code
# entirely and still have a working function. Also, the line "answer = total" is
# unnecessary and can be taken out, with "return total" being used instead (see 
# below).

def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''
    total = 0
    for item in lst:
        total += item
    return total
