#7.B.1.1:

def union(s1, s2):
    '''Computes and returns the set union of the input sets s1 and s2 (i.e., all
    elements that are in either set). The input sets can also be frozensets.'''
    s3 = set({})
    for e in s1:
        s3.add(e)
    for e in s2:
        s3.add(e)
    return s3

#7.B.1.2:

def intersection(s1, s2):
    '''Computes and returns the set intersection of the input sets s1 and s2 
    (i.e., all elements that are in both sets). The input sets can also be 
    frozensets.'''
    s3 = set({})
    for e in s1:
        if e in s2:
            s3.add(e)
    return s3

#7.B.2:

def mySum(*x):
    '''Computes and returns the sum of the arbitrary number of inputs. Raises
    a ValueError if one of the inputs is less than 0, and a TypeError if an 
    input is not an integer.'''
    total = 0
    for k in x:
        if type(k) is not int:
            raise TypeError('Inputs must be integers!')
        elif k <= 0:
            raise ValueError('Inputs must be positive!')        
        else:
            total += k
    return total
    
#7.B.3:

def myNewSum(*x):
    '''Performs the same function as "mySum" defined above, but also works on 
    single lists of integers in addition to an arbitrary number of integer 
    inputs. Also throws errors if the elements of the list (or arbitrary number
    of inputs) are not positive integers.'''
    total = 0
    if len(x) > 0 and type(x[0]) is list and len(x) == 1:
        for k in x[0]:
            if type(k) is not int:
                raise TypeError('Inputs must be integers or lists of integers!')
            elif k <= 0:
                raise ValueError('Inputs must be positive!') 
            else:
                total += k
        return total
    else:
        for k in x:
            if type(k) is not int:
                raise TypeError('Inputs must be integers or lists of integers!')
            elif k <= 0:
                raise ValueError('Inputs must be positive!')        
            else:
                total += k
        return total            

#7.B.4:

def myOpReduce(intList, **op):
    '''Takes the input list of integers intList and returns their sum if the 
    keyword \'op\' is a \'+\', their product if it is a \'*\', and the maximum
    value in the list if it is \'max\'. Raises various ValueErrors if there is
    no keyword given, if there are multiple keywords given, if the keyword given
    is invalid, or if the keyword argument is not a string.'''
    if len(op) == 0:
        raise ValueError('No keyword argument given.')
    elif len(op) > 1:
        raise ValueError('Too many keyword arguments given.')
    elif op.keys()[0] != 'op':
        raise ValueError('Invalid keyword argument given.')    
    elif type(op['op']) is not str:
            raise TypeError('Value for keyword argument \'op\' must be a string.')    
    elif op['op'] == '+':
        total = 0
        for n in intList:
            total += n
        return total
    elif op['op'] == '*':
        product = 1
        for n in intList:
            product *= n
        return product
    elif op['op'] == 'max':
        if len(intList) == 0:
            return 0
        else:
            largest = intList[0]
            for n in intList:
                if n > largest:
                    largest = n
            return largest
    else:
        raise ValueError('Invalid keyword argument given.')

# 7.C.1: The issue with this code is that it quits the program entirely if a 
# KeyError is raised when referencing key1 and key2. Also, this function seems 
# minor relative to any kind of decent sized program, so an error raised within
# it should be handled by a try/except block in a different function. Therefore,
# this function should simply allow the KeyError to happen, rather than raising
# an error or attempting to handle the error itself. This is shown below:

import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.
    '''
    return dict[key1] + dict[key2]
        
# 7.C.2: The same kind of issue as in 7.C.1 occurrs in this function. This 
# function does not need to catch the KeyError it may throw, and it should 
# instead allow another function to handle this error. Therefore, it should 
# simply allow the KeyError to happen. This is shown below:

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.
    '''
    return dict[key1] + dict[key2]
        
# 7.C.3: The error in this code is that the except block it contains is 
# useless. Because the code catches the KeyError only to simply raise it again
# if caught, it is useless to even have the try/except block to begin with, and
# should simply contain the return line. This is shown below.

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.
    '''
    return dict[key1] + dict[key2]

# 7.C.4: The issue with this code is that, similar to 7.C.3, it catches an 
# exception only to raise it again. This is useless and inefficient, as the code
# could simply allow the exception to happen on its own and not except it. It
# also doesn't really need to define val1 and val2 objects, as it could simply
# return the sum in the way the other three functions did. This is shown below:

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.
    '''
    return dict[key1] + dict[key2]

# 7.C.5: The issue with this code is that it raises an error (which is fine as 
# long as another function handles it) and then attempts to print the error out
# to the stderr. Because the error has already been raised, the print statement
# will never be reached. Also, if an error is going to be raised and a different
# function is going to handle it, then this function should not also try to 
# handle it by printing it out. Thus, the print statement can be removed, as 
# shown below:

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# 7.C.6: The issue with this code is similar to the issue in 7.C.5. The code 
# attempts to raise an exception (for another function to handle) and also 
# handle the exception itself. The difference here is that the print line will
# actually execute, whereas in 7.C.5 it did not. The way to fix it is still the
# same, though: simply remove the print line from the code and only raise the
# ValueError for another function to handle. This is shown below:

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)
    
# 7.C.7: The issue with this code is that it raises the wrong type of error. 
# Rather than raising a TypeError, this code should raise a ValueError to 
# reflect the fact that the value of x given is invalid.

from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)

# 7.C.8: The issue with this code is that it does not give specific enough 
# exceptions. If an exception raised by this function is to be handled by 
# another function, it must give more specific information about the type of
# error raised, so that the function can handle each case differently. This 
# function could do this by raising a TypeError and a ValueError, respectively,
# as shown below in order to be more specific.

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if type(x) is not float:
        raise TypeError('x must be a float')
    elif x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)

