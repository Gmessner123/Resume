# Name: Grant Messner
# CMS cluster login name: gmessner

# Part 1: Pitfalls


# Question 1.1:

# Error 1: In the "elif" statement, this code mistakenly uses the "=" operator 
# instead of the "==" operator to determine whether n is divisible by 2. This 
# will result in a syntax error, as "=" is used for assigning variables, not for
# assessing equality.

# Error 2: In the "if" statement, this code forgets to put an "n" before the 
# "== 3". This results in a syntax error, because python does not know that 
# the "== 3" is necessarily referring to the variable "n".

# Error 3: In the "else" statement, the code forgets to put a ":" after the word
# "else". This results in a syntax error as colons are needed after all if, 
# elif, and else statements.

# Error 4: This function uses the wrong syntax for writing its docstring. It 
# uses two double quote (") characters, rather than the ''' character, resulting
# in a syntax error.

# Error 5: Overall, this function uses too much indentation for its body 
# relative to its attempt at a docstring. Because it changes spacing from the 
# commas in the docstring (although they should be triple quotes), without 
# introducing some kind of a loop or statement (like a "for" loop or "if"
# statement), it causes an error.


# Question 1.2: 

# Error 1: The first issue with this code is the fact that the first function 
# does not define the variable "result" before using it in the statement
# "result = n * result". Thus, the code will give an error when it is ran 
# because result has not yet been defined (i.e., a variable cannot be first 
# defined using the variable name itself). To fix this, the value of result  
# should be set to n before the "while" loop is called.

# Error 2: The second error that occurs here is that the first function uses the 
# keyword return inside of its "if" statement, when it really needs to use the
# keyword "break" to escape the "while" loop. Thus, the way the function works
# right now, the function simply returns nothing when n becomes less than 0,
# rather than actually computing the factorial of n.

# Error 3: The third error occurs in the first function as well, as it prints
# the factorial of n, rather than returning it. Because the docstring indicates
# that it should return this value, the "print" statement should be replaced 
# with a "return" statement.

# Error 4: The fourth error occurs in the first function. In the case of n == 0,
# the function returns 0, when it is supposed to return 1 (assuming errors 1-3
# have been corrected). To fix this, the function should include a special case 
# for n == 0, using an "if n == 0 :" statement before the "while" loop to check.
# If n is indeed zero, there should be a "return 1" statement inside of the 
# "n == 0" statement, to ensure that the function never even gets to the while
# loop before it returns 1.

# Error 5: The last error is also in the first function. Since the factorial 
# function (in mathematics) is only defined for domain of non-negative integers,
# our Python function should not produce any output for values of n. Thus, this
# function needs another assert statement such as "assert int(n) == n" to make
# sure that it can only be called on non-negative integer values of n.


# Question 1.3:

# Error 1: The first mistake this function makes is that it uses a name that is 
# not descriptive of what the function actually does (it is just named "w").
# This makes it difficult for whoever is reading the code to understand what 
# this function actually is supposed to be doing.

# Error 2: This function does not correctly format its docstring, and the 
# wording of the docstring does not make any sense. The docstring should be 
# enclosed by triple quotes ('''), and should provide descriptive information
# about the function, neither of which this one does (i.e., it is enclosed by
# double quotes and contains jibberish).

# Error 3: Throughout this function, there is no space left between binary 
# operators (i.e., between +, =, etc.). This makes the code somewhat difficult
# to read.

# Error 4: This function does not use consistent indentation for the code within
# its if/else statements. The statement "v += [i]" and the statement "i = i" 
# should be indented the same amount, but in this code they are not.

# Error 5: This function also contains a block of usesless code (the else: i = i
# block). Because this block simply assigns the value of i to itself, it is 
# unnecessary and should be removed to make the code more concise.



# Part 2: Writing simple functions

# Question 2.1:

def draw_box(n):
    '''Prints out an (n+2) x (n+2) box with the following specifications: 
    1. The corners of the box are '+' characters. 2. The sides of the box are
    '-' characters (horizontal sides) or '|' characters (vertical sides). 3. The
    interior of the box is filled with alternating 'x' and 'o' characters in a 
    right triangle pattern along the bottom and left sides of the box, as well
    as along the diagonal of the box.'''
    s = '\n'
    assert n > 0 , 'Box sides must be positive'
    for i in range(0, n + 2):
        for j in range(0 ,n + 2):
            if i == 0 or i == n+1:
                if j == 0 or j == n + 1:
                    s += '+'
                else:
                    s += '-'
            else:
                if j == 0 or j == n + 1:
                    s += '|'
                elif j > i:
                    s += ' '
                elif j % 2 == 0:
                    if i % 2 == 0:
                        s += 'x'
                    else:
                        s += 'o'
                else:
                    if i % 2 == 0:
                        s += 'o'
                    else:
                        s += 'x'
                    
            if j == n + 1:
                s += '\n'            
    return s


# Question 2.2.1:

import random as r

def hypervolume(d, nmax):
    '''Approximates the hypervolume of the d-dimensional hypershpere using the 
    Monte-Carlo approximation with nmax points. Computes the number of randomly
    generated points that lie in the N-sphere 
    (x_1)^2 + (x_2)^2 + ... + (x_N)^2 <= 1, then divides that number by the 
    total number of generated points (nmax). This ratio, multiplied by the value
    2 ** d (where d is the number of dimensions, gives us the hypervolume of the
    N-sphere.'''
    count = 0
    for i in range(0, nmax):
        squareSum = 0
        for j in range(0 , d):
            squareSum += (r.random() ** 2)  
        if squareSum <= 1:
            count += 1
    ratio = float(count) / float(nmax)
    return ratio * (2 ** d)

# Question 2.2.2:

import math

def correct_hypervolume(d):
    '''
    Compute the hypervolume of a hypersphere of dimension 'd' and radius = 1.

    Argument: d (number of dimensions (>= 2))
    Return value: the hypervolume
    '''
    assert d >= 2, 'Number of dimensions must be at least 2'
    if d == 2:
        return math.pi
    elif d == 3:
        return 4.0 / 3.0 * math.pi
    else:
        return (2.0 * math.pi / d) * correct_hypervolume(d - 2)
    
def print_hypervolumes(dmax, nmax):
    '''Prints out the an estimated hypervolume, a theoretical hypervolume, and 
    the percentage error between the two for every dimension d in the integer 
    range [2, dmax], using the Monte-Carlo approximation with nmax points.'''
    print 'Iterations: %d' % nmax
    print '\n'
    for d in range(2, dmax + 1):
        estimate = hypervolume(d, nmax)
        theoretical = correct_hypervolume(d)
        error = (abs(theoretical - estimate) / theoretical) * 100
        errorString = str(error) + '%'
        print 'dimension: %d' % d
        print 'estimated hypervolume: %f' % estimate
        print 'correct hypervolume: %f' % theoretical
        print 'error: %s ' % errorString
        print '\n'
        
# Question 2.3:

def encode(s):
    '''Encodes all of the vowels in the given string s by interchanging them for
    words given in the following table: 
    
    a --> at
    e --> eat
    i --> iota
    o --> outer
    u --> uniter'''
    d = {'a': 'at','e':'eat','o':'outer','i':'iota','u':'uniter'}
    s2 = s
    for key in d:
        if key in s:
            s2 = s2.replace(key, d[key])
    return s2

def decode(s):
    '''Decodes the given encoded string s by exchanging all of the encoded words
    withing the string with their corresponding letters, based on the following
    table:
    
    at --> a
    eat --> e
    iota --> i
    outer --> o
    uniter --> u
    '''    
    dInverse = {'eat':'e','at': 'a', 'iota':'i', 'outer':'o', 'uniter':'u'}
    s2 = s
    for key in dInverse:
        if key in s:
            s2 = s2.replace(key, dInverse[key])
    return s2



# Part 3: Miniproject: Chaos theory

# Question 3.1:

def logistic_iter(r, x, niters, nsave):
    '''Returns a list representing the last nsave iterations (out of niters 
    total iterations) of the logistic function L(x) = r * x * (1-x) for the 
    given input values of r and x. This function will thus be outputting 
    numerical values, rather than iterated functions.'''
    assert r > 0.0,'Function only works for positive r-values'
    assert x>= 0.0 and x <= 1.0,'x parameter must be in the interval [0.0, 1.0]'
    assert nsave >= 0 and nsave <= niters,'nsave must be within [0.0, niters]'
    
    xNow = x
    saveList = []
    for i in range(0, niters):
        xNow = r * xNow * (1-xNow)
        if i >= (niters - nsave):
            saveList.append(xNow)
    assert nsave == len(saveList)
    return saveList

# Question 3.2:
    
def logistic_time_series(rs, x, niters, nsave, filename, yrange):
    '''After opening up the file filename, writes the output of logistic_iter
    line-by-line for each value of r in rs (i.e., each line has an element of 
    the output list from logistic_iter from each r in rs). It also opens a 
    similar file in gnuplot and writes the instructions for how to plot output 
    for each value of r. The parameters x, niters, and nsave are only used to 
    call logistic_iter, and have the same function as before.'''
    file1 = open(filename, 'w')
    bigList = []
    for i in range(0, nsave):
        j = 0
        line = str(i) + ' '
        for r in rs:
            bigList.append(logistic_iter(r, x, niters, nsave))
            line += str(bigList[j][i]) + ' '
            j += 1
        file1.write(line)
    file1.close()
    
    # Generate the gnuplot script file.
    file = open(filename + '.gp', 'w')
    if yrange != 'auto':
        print >> file, 'set yrange [0:1]'
    for (i, r) in enumerate(rs):
        print >> file, 'set title "r = %g" font ",24"' % r
        print >> file, 'set nokey'
        print >> file, "set style line 1 lc rgb 'blue' pt 6 ps 1.5"
        print >> file, 'plot "%s" using 1:%d with linespoints ls 1' % \
            (filename, i+2)
        print >> file, 'pause -1 "hit any key to continue..."'
        print >> file
    file.close()    
    
# Question 3.3:

def find_period(r, x, niters, nsave, precision):
    '''Determines the period of the logistic function with the given parameters.
    The values r, x, niters, and nsave are as before in logistic_iter. Here, the
    precision parameter is the range within which two values will be considered
    the same when calculating the period of the logistic function. Returns the
    period of the function, or returns -1 if the function exhibits chaotic 
    behavior.'''
    allValues = logistic_iter(r, x, niters, nsave)
    occurred = []
    occurred.append(allValues[0])
    for i in range(0, nsave):
        isUnique = True
        for j in range(0, len(occurred)):
            if abs(occurred[j] - allValues[i]) < precision:
                isUnique = False
        if isUnique == True:
            occurred.append(allValues[i])
    if len(occurred) != nsave:
        return len(occurred)
    else:
        return -1

# Question 3.4:

def is_power_of_two(n):
    '''Returns True if the given input value n is a power of 2 (up to 4096), 
    False otherwise.'''
    return n in [1,2,4,8,16,32,64,128,256,512,1024,2048,4096]

def find_bifurcation_point(x, niters, nsave, prec1, prec2, period):
    '''Calculates the bifurcation point (a value of r) of the function within 
    the range of prec2. The parameters x, niters, nsave are all as specified in
    logistic_iter, and prec1 is the precision parameter to find_period. The 
    period parameter is the period to find the bifurcation point at. This
    function uses a binary search algorithm to find the period.'''
    low = 0.0
    high = 4.0
    mid = 2.0
    while (high - low) > prec2:
        mid = (high + low) / 2
        per = find_period(mid, x, niters, nsave, prec1)
        if (per < period) and is_power_of_two(per) == True:
            low = mid
        else:
            high = mid        
    return low

# Question 3.5:

def find_feigenbaum_constant(x, niters, nsave, prec1, prec2, period):
    '''Gives repeated estimates for the feigenbaum constant by repeatedly 
    calling the find_bifurcation_point function on increasing values of 2 ** n 
    (the period). Prints out these values one at a time, along with the maximum 
    value of 2 ** n, line by line. All parameters are the same as they were in 
    find_bifurcation_point, except period here refers to the maximum period 
    value used in the estimate.'''
    power = 2
    while (power * 4) <= period:
        b1 = find_bifurcation_point(x, niters, nsave, prec1, prec2, power)
        b2 = find_bifurcation_point(x, niters, nsave, prec1, prec2, power * 2)
        b3 = find_bifurcation_point(x, niters, nsave, prec1, prec2, power * 4)
        estimate = (b2 - b1) / (b3 - b2)
        s = '%d     %f'%(power * 4, estimate)
        print s
        power *= 2
        
           