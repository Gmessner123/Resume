'''Test script for assignment 7, section B.'''

import nose
from nose.tools import assert_raises
from lab7_bc import *

def test_union():
    s1 = {1, 2, 3}
    s2 = {4, 5, 6}
    s3 = {1, 3, 5}
    assert union(set(), set()) == set()
    assert union(s1, set()) == s1
    assert union(s2, set()) == s2
    assert union(s1, s2) == {1, 2, 3, 4, 5, 6}
    assert union(s1, s3) == {1, 2, 3, 5}
    assert union(s2, s3) == {1, 3, 4, 5, 6}
    assert union(frozenset(), frozenset()) == frozenset()
    assert union(s1, frozenset()) == s1
    assert union(s2, frozenset()) == s2
    assert union(s1, s2) == frozenset([1, 2, 3, 4, 5, 6])
    assert union(s1, s3) == frozenset([1, 2, 3, 5])
    assert union(s2, s3) == frozenset([1, 3, 4, 5, 6])
    assert type(union(s2, s3)) == type(set())

def test_intersection():
    s1 = {1, 2, 3}
    s2 = {4, 5, 6}
    s3 = {1, 3, 5}
    assert intersection(set(), set()) == set()
    assert intersection(s1, set()) == set()
    assert intersection(s2, set()) == set()
    assert intersection(s1, s2) == set()
    assert intersection(s1, s3) == {1, 3}
    assert intersection(s2, s3) == {5}
    assert intersection(frozenset(), frozenset()) == frozenset()
    assert intersection(s1, frozenset()) == set()
    assert intersection(s2, frozenset()) == set()
    assert intersection(s1, s2) == frozenset()
    assert intersection(s1, s3) == frozenset([1, 3])
    assert intersection(s2, s3) == frozenset([5])
    assert type(intersection(s2, s3)) == type(set())

def test_mySum():
    assert mySum(1, 2, 3, 4, 5) == 15
    assert mySum() == 0
    assert_raises(ValueError, mySum, 2, -1, 3)  
    assert_raises(TypeError, mySum, [1, 2, 3])  

def test_myNewSum():
    assert myNewSum(1, 2, 3, 4, 5) == 15
    assert myNewSum(1) == 1
    assert myNewSum() == 0
    assert_raises(ValueError, myNewSum, 2, -1, 3)
    assert_raises(ValueError, myNewSum, 0, 2, 3)
    assert_raises(TypeError,  myNewSum, 'foo', 'bar')
    assert myNewSum([1, 2, 3]) == 6
    assert_raises(TypeError,  myNewSum, ['foo', 'bar'])
    assert_raises(ValueError, myNewSum, [1, 0, -1])
    assert_raises(TypeError,  myNewSum, 1, 2, 3, [4, 5, 6])
    assert_raises(TypeError,  myNewSum, [1, 2, 3], [4, 5, 6])

def test_myOpReduce():
    assert myOpReduce([1, 2, 3, 4, 5], op='+') == 15
    assert myOpReduce([], op='+') == 0
    assert myOpReduce([1, 2, 3, 4, 5], op='*') == 120
    assert myOpReduce([], op='*') == 1
    assert myOpReduce([1, 2, 3, 4, 5], op='max') == 5
    assert myOpReduce([], op='max') == 0
    assert_raises(ValueError, myOpReduce, [1, 2, 3, 4, 5])
    assert_raises(ValueError, myOpReduce, [1, 2, 3, 4, 5], op='foo')
    assert_raises(TypeError,  myOpReduce, [1, 2, 3, 4, 5], op=123)
    assert_raises(ValueError, myOpReduce, [1, 2, 3, 4, 5], bla='+')
    assert_raises(ValueError, myOpReduce, [1, 2, 3, 4, 5], op='+', bla='foo')

if __name__ == '__main__':
    nose.runmodule()


