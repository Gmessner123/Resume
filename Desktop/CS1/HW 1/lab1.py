#C.1.1: 9 - 3 --> 6
#C.1.2: 8 * 2.5 --> 20.0
#C.1.3: 9 / 2 --> 4
#C.1.4: 9 / -2 --> -5
#C.1.5: 9 % 2 --> 1
#C.1.6: 9 / -2 --> -1
#C.1.7: -9 / 2 --> 1
#C.1.8: 9 / -2.0 --> -4.5
#C.1.9: 4 + 3 * 5 --> 19
#C.1.10: (4 + 3) * 5 --> 35

#C.2.1: x--> 100 
#C.2.2: x--> 110
#C.2.3: x--> 130
#C.2.4: x--> 90
#C.2.5: x--> 40
#C.2.6: x--> 120
#C.2.7: x--> 24
#C.2.8: x--> 0

#C.3: After this statement evaluates, x has a final value of 3. The first step
#that occurs is that the expression x += y is converted to x=x+y, where y is the
#quantity (x-x) in this case. Thus, we have x=x+(x-x). Since the expression 
#inside of the parentheses, x-x, is evaluated first, this is evaluated to 0 
#because 3-3 is evaluated to 0. Thus, we have x=x+0, which is equivalent to x=x.
#Thus, we assign x to its original value, and by the end of this process x is 
#assigned to 3.

#C.4.1: 3.4j
#C.4.2: (-16 + 0j)
#C.4.3: (0.44 + 0.08j)
#C.4.4: (-3 + 4j)
#C.4.5: (1 + 4j)
#The difference in answers in the previous two parts arises from the fact that
#the first one used parentheses, and the second one did not. Thus, the 
#expressions on the inside of the parentheses are "FOIL"-ed together (i.e.,
#1*1+2j*1+1*2j+2j*2j). In the second problem, parentheses are not used, and 
#the expression is thus evaluated via standard order-of-operations rules (i.e,
#2j*1 is the only multiplication form. Thus, python evaluates complex numbers 
#similarly to how it evaluates real numbers using order-of-operations.

#C.5.1: (-3.165778513216168 + 1.959601041421606j)
#C.5.2: (1.2652585805200263 + 1.856847768512215j)
#C.5.3: (-1 + 1.2246467991473532e-16j)
#It is a better idea to import without including the * symbol because although 
#the *  symbol imports the entire library without requiring you to qualify each
#method (i.e., write something like sin(x) instead of math.sin(x)), it can 
#result in "name clashes" if two different libraries are imported using the
#* symbol and have the same methods. That is, if math and cmath both have the
#sin(x) method, then the cmath version will automatically be used in this case,
#because the cmath library was imported last.

#C.6.1: 'foobar'
#C.6.2: 'foobar'
#C.6.3: 'foobar'
#C.6.4: Traceback (most recent call last):
 # Python Shell, prompt 48, line 1
#invalid syntax: <string>, line 1, pos 3

#C.7.1: 'A\nB\nC'

#C.8.1: 80 * '-'

#C.9.1: 'first line\nsecond line\nthird line'

#C.10.1-5:
x = 3
y = 12.5
print 'The rabbit is %d.' % x
print 'The rabbit is %d years old.' % x
print '%g is average.' % y
print '%g * 3' % y
print '%g * 3 is 37.5.' % y

#C.11.1: 
raw = raw_input('Enter a number: ')
num = float(raw)
print num

#C.12.1:
def quadratic(a,b,c,x): 
    '''Returns the quadratic function ax^2+bx+c evaluated at for the given
    parameters a,b,c, and x.'''
    return a * x * x + b * x + c

def GC_content(S):
    '''For a given DNA string S (composed of bases 'A', 'G','C', and 'T'),
    computes the ratio of G and C counts to the total number of counts of each
    letter in S. This ratio is returned by the function.'''
    num_A = S.count('A')
    num_G = S.count('G')
    num_C = S.count('C')
    num_T = S.count('T')
    a = float(num_A)
    g = float(num_G)
    c = float(num_C)
    t = float(num_T)
    return (g + c) / (a + g + c + t)

#I apologize in advance if the spaces between +,-,*, and / operators aren't
#included in assignment 2: I didn't see your comments on this assignment until
#after I already submitted assingment 2.