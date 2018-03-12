import random

#B.1.1

def complement(s):
    '''Returns the complement of a given DNA string (i.e., changes all 
    A's to T's and G's to C's, and vice versa).'''
    s1=''
    for c in s:
        if c=='A':
            s1+='T'  
        elif c=='T':
            s1+='A'
        elif c=='G':
            s1+='C'
        elif c=='C':
            s1+='G'
            
    return s1


#B.2.1

def list_complement(l):
    '''Converts the input DNA list into its complement DNA list, using the
    same rules as specified in the "complement" method.'''
    for i in range(0,len(l)):
        if l[i]=='A':
            l[i]='T'
        elif l[i]=='T':
            l[i]='A'
        elif l[i]=='G':
            l[i]='C'
        elif l[i]=='C':
            l[i]='G'

#B.3.1

def product(l):
    '''Computes the product of the input list of numbers.'''
    prod=1
    for i in l:
        prod*=i
        
    return prod


#B.4.1

def factorial(n):
    '''Computes the factorial of the given input n (i.e., computes
    n*(n-1)*(n-2)*...*2*1).'''
    nums=range(1,n+1)
    return product(nums)


#B.5.1
def dice(m,n):
    '''Computes the sum of a random roll of n dice with m number of sides.'''
    nums=range(1,m+1)
    sum=0
    i=0
    while i<n:
        sum+=random.choice(nums)
        i+=1
        
    return sum


#B.6.1

def removeAll(lst,n):
    '''Removes all elements n from the list lst.'''
    while lst.count(n)>0:
        lst.remove(n)
        

#B.7.1


def removeAll_2(lst,n):
    '''Removes all elements n from the list lst. Counts the number of 
    occurrances first, then iterates through that many times to remove 
    the elements.'''
    count=lst.count(n)
    for i in range(0,count):
        lst.remove(n)
        
    
            

def removeAll_3(lst,n):
    '''Removes all elements n from the list lst. Removes elements one by one
    as long as there is at least one occurance in the list.'''
    while n in lst:
        lst.remove(n)
        
    
    
#B.8.1

def any_in(l1, l2):
    '''Determines if any elements in the first list are equal to any 
    of the elenents in the 2nd list.'''
    for c1 in l1:
        for c2 in l2:
            if c1==c2:
                return True
            
    return False


#C.1.a: The problem here is that the code uses the "=" instead of the "=="
#to test for equality. The "=" is used to assign one value to another, not
#to test if two values are equal (that is what the "==" is used for), and thus
# the "==" should have been used.

#C.1.b: This code is wrong because it uses the actual letter 's' as the 
#argument to the function, not the general string s, causing an error. If a string
#is used as an argument of a function, it cannot have a value assigned to it
#already (like 's'). Thus, this code could be fixed by changing the 's' in the 
#argument of the function to just an s.

#C.1.c: This code does not cause any runtime errors, but it does not output
#the desired value of the string s concatanated with the suffix '-Caltech'. 
#Rather, this code concatanates the literal string 's' with the suffix instead.
#To fix this, simply change the 's' with the string s.

#C.1.d: This code does not work because it attempts to add two different types
#of objects together (list and string). While the "+" operator is overloaded,
# it does not support the addition of lists with strings. In order to add a 
#string as an element of the list, this code should have used lst.append('bam').

#C.1.e: The issue with this code is that the list functions reverse() and 
#append() do not return any values (they instead just modify the existing list
#that they are called on). Thus, assigning a value such as "lst2" to "lst.reverse()"
#is not allowed. This could be fixed by simply calling lst.reverse() and then
#lst.append(0) and returning lst at the end of the function.

#C.1.f: The problem with this function is that it uses the reserved words "str"
#and "list" as arguments. These words are used to designate the Python objects
#string and list, and cannot be used as variable names. Thus, this code could 
#be fixed by using the variables s and l instead of str and list. Also, this
#code does not append the letters correctly, even once the variable names are
#fixed. The code appends the entire string (in list form) to the original list,
#rather than appending the string letter by letter. To fix this, the code could
#instead run a "for" loop over the input string once it is converted into a list,
#appending each element of the string (as a list) into the original input list.


#C.2.1: The reason this code prints 30 instead of 50 is that the value of c is
#not retroactively changed with the updated value of a. In other words, when
#Python executes the line c=b+a, it creates an object c and gives it the value
#of whatever the quantity a+b is at the particular moment. So in our case, the
#object c is created and given the value of 30. Therefore, even when the value
#of a is changed after the object c is created, the value of c is not affected.


#C.3.1: The reason why the first function would work, while the second one would
#not, is because the first one actually returns a value, whereas the second one
#only prints one out. Printing a value displays the value in the Python
#shell window, but does not output a value that a variable can be assigned to,
#whereas returning a value does the opposite (i.e., prints nothing but outputs
#a value that can be used later on in the code that can be assigned to a variable
#or object). Thus, the function that returns a value (add_and_double_1) is able
#to be manipulated as any other variable can be, and can thus be doubled and
#assigned to the variable n. However, the function add_and_double_2 does not
#return anything and can thus not be manipulated as if it were another variable
#or object, and so multiplying add_and_double_2(1, 2, 3) by 2 and assigning it
#to n is not allowed.

#C.4.1: The reason why the second function does not work, while the first one does,
#in executing then n=2*num_of_squares(2,3) lines is that the second function does
#not take any input parameters, while the first one does. Thus, attempting to call
#sum_of_squares_2(2,3) results in an error, because sum_of_squares_2() expects no
#arguments. The key difference between these two functions is that sum_of_squares_1()
#allows the programmer to directly type in the arguments, whereas sum_of_squares_2()
#relies on user input to obtain its x and y values. The sum_of_squares_2() method
#would work perfectly fine if the programmer wrote n = 2 * sum_of_squares_2() with
#no arguments, instead of n = 2 * sum_of_squares_2(2, 3). However, as it is now,
#the code n = 2 * sum_of_squares_2(2, 3) does not work because sum_of_squares_2()
#expects no arguments.

#C.5.1: This function does not work because it is written as if the string s
#can be treated as a list. When working with lists, the syntax l[0] is allowed
#to reference a specific element of the list, but Python does not support this 
#type of syntax for referencing specific characters in a string. 

#C.6.1: The reason this function doesn't actually double all of the elements in
#the list is because the for loop over the list does not actually access the 
#value of each element in the list. Rather, it accesses a variable item that
#takes on the value of each element in the list, but does not allow each value
#to be changed. Thus, this type of loop can extract information about the contents
#of the list, but cannot actually modify the list itself. In order to actually 
#modify the elements of the list itself, the for loop should loop a variable 
#(call it i) over range(0,len(lst)) and execute lst[i]*=2 with each iteration.
#This will directly change each element of the list, rather than just changing
#the variable assigned to represent each element (in this case, the variable item).
   
