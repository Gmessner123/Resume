
def list_reverse(l):
    '''Returns a reversed version of the given list l, leaving the contents of
    l unchanged.'''
    l2 = l[:]
    l2.reverse()
    return l2

def list_reverse2(l):
    '''Returns a reversed version of the given list l, leaving the contents of
    l unchanged. Uses a for loop to loop over l in reverse.'''
    l2 = []
    
    for i in range(len(l)-1,-1,-1):
        l2.append(l[i])
        print i
        
    return l2

def file_info(f):
    '''Returns a tuple representing the line count, word count, and character 
    count of the file (i.e., (lc,wc,cc)).'''
    f1 = open(f,'r')
    lc = 0
    wc = 0
    cc = 0
    
    while True:
        line = f1.readline()
        if line == '':
            f1.close()
            break
        lc += 1
        cc += len(line)
        wc += len(line.split()) 
        
    t = (lc,wc,cc)
    return t

def file_info2(f):
    '''Returns a tuple representing the line count, word count, and character 
    count of the file (i.e., (lc,wc,cc)).'''
    f1 = open(f,'r')
    lc = 0
    wc = 0
    cc = 0
    
    while True:
        line = f1.readline()
        if line == '':
            f1.close()
            break
        lc += 1
        cc += len(line)
        wc += len(line.split())
        t = (lc,wc,cc)
        d = {'lines: ': t[0], 'words': t[1], 'characters': t[2]} 
        
    return d

def longest_line(f):
    '''Returns a tuple of the form (length, line) of the longest line in the
    file, along with its length.'''
    f1 = open(f,'r')
    lmax = ''
    lenmax = 0
        
    while True:
        line = f1.readline()
        if line == '':
            break
        if len(line) > lenmax:
            lenmax = len(line)
            lmax = line
    return (lenmax , lmax)

def sort_words(s):
    '''Sorts the string into a list of words in alphabetical order.'''
    l = s.split()
    l.sort()
    return l


#B.7.1: 11011010 in binary is equivalent to 0*2^0 + 1*2^1 + 0*2^2 + 1*2^3 + 
#1*2^4 + 0*2^5 + 1*2^6 + 1*2^7, which give us a decimal answer of 218. The 
#largest 8 digit binary number, 11111111, is equivalent to 255 in decimal.


def binaryToDecimal(l):
    '''Returns the decimal form of the input binary number (in list form).'''
    sum = 0
    for i in range(len(l)-1, -1, -1):
        sum += l[i] * 2 **(len(l)-i-1)
        
    return sum

#Honor Roll problem
def decimalToBinary(n):
    '''Returns a list representing the binary form of the input decimal number 
    (inputted as a number).'''
    lst = []
    i = 1
    k = 0 
    
    while i <= n:
        i *= 2
        k += 1
    
    while k >= 1:
        if n >= (2 ** (k-1)):
            lst.append(1)
            n -= (2 ** (k-1))
        else:
            lst.append(0)
            
        k -= 1
    
    return lst

# C.2.1: The three errors in this code are (1) it doesn't leave space between
# the '+' and '*' binary operators, making the code difficult to read. (2) This
# code also doesn't put space after commas in the argument of the function. (3)
# Lastly, this code uses a function name that isn't very descriptive, making it
# hard for somebody to simply glance at the function and understand what it is
# doing. In addition, no Docstring is given describing the function. Corrected 
# code is shown below:

def sumOfCubes(a, b, c): 
    '''Returns the cubic sum a^3 + b^3 + c^3 of the arguments a, b, and c.'''
    return a * a * a + b * b * b + c * c * c

# C.2.2: The four errors in this code are (1) the function is poorly named 
# because it is hard to tell the difference between the words "sum," "of," and 
# "cubes" (none of the words are capitalized). (2) The function attempts to 
# write a Docstring, but uses improper syntax (# instead of ''') and several
# spelling mistakes. (3) This function also uses argument names that are 
# unnecessarily long ("argumenta, argumentb," etc.), making it hard to read. (4)
# This function also exceeds the 80 character maximum for a given line with its 
# excessively long return statement. Corrected code is shown below:

def SumOfCubes(a, b, c, d):
    '''Returns the cubic sum a^3 + b^3 + c^3 + d^3 of the arguments a, b, c,
    and d.'''
    return a * a * a + b * b * b + c * c * c + d * d * d

# C.2.3: The two errors in this code are (1) there is no blank line left in 
# between the two functions, making the code hard to read. (2) The two different
# functions use indentation that is inconsistant from one another (i.e., the
# first function indents farther than the second function in the main function
# body). This gives the code a sloppy appearence. Also, no Docstring is given in
# either function. Corrected code is shown below:

def sum_of_squares(x, y):
    '''Returns the square sum x^2 + y^2 of the arguments x and y.'''
    return x * x + y * y

def sum_of_three_cubes(x, y, z):
    '''Returns the cubic sum x^2 + y^2 + z^2 of the arguments x, y, and z.'''
    return x * x * x + y * y * y + z * z * z
