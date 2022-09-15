# lab4_b_tests.py

import nose
from lab4_b import *

def test_random_size():
    for i in range(100):
        n = random_size(0, 100)
        assert n >= 0 and n <= 100
        assert n % 2 == 0

def test_random_position():
    for i in range(100):
        (x, y) = random_position(800, 600)
        assert 0 <= x <= 800 and 0 <= y <= 600

def test_random_color():
    for i in range(100):
        col = random_color()
        col = col.lower()
        assert len(col) == 7
        assert col[0] == '#'
        for i in range(1, 7):
            assert col[i] in ['0', '1', '2', '3', '4', '5', '6', '7', 
                              '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

def test_count_values():
    assert count_values({}) == 0
    assert count_values({ 'foo' : 1, 'bar' : 2, 'baz' : 3 }) == 3
    assert count_values({ 'foo' : 1, 'bar' : 1, 'baz' : 2 }) == 2
    assert count_values({ 'foo' : 2, 'bar' : 1, 'baz' : 2 }) == 2
    assert count_values({ 'foo' : 1, 'bar' : 1, 'baz' : 1 }) == 1

def test_remove_value():
    d = {}
    remove_value(d, 'foo')
    assert d == {}

    d = { 'foo' : 1, 'bar' : 2, 'baz' : 3 }
    remove_value(d, 4)
    assert d == { 'foo' : 1, 'bar' : 2, 'baz' : 3 }

    d = { 'foo' : 1, 'bar' : 2, 'baz' : 3 }
    remove_value(d, 2)
    assert d == { 'foo' : 1, 'baz' : 3 }
    remove_value(d, 3)
    assert d == { 'foo' : 1 }
    remove_value(d, 1)
    assert d == {}

def test_split_dict():
    d1, d2 = split_dict({})
    assert d1 == {}
    assert d2 == {}
    d1, d2 = split_dict({ 'Jim' : 1, 'Tom' : 2, 'Sam' : 3, 'Bob' : 4 }) 
    assert d1 == { 'Jim' : 1, 'Bob' : 4 }
    assert d2 == { 'Tom' : 2, 'Sam' : 3 }
    d1, d2 = split_dict({ 'Rat' : 'animal', 'space' : 'bar',
                          'cup' : 'utensil', 'Green' : 'color' })
    assert d1 == { 'cup' : 'utensil', 'Green' : 'color' }
    assert d2 == { 'Rat' : 'animal', 'space' : 'bar' }

def test_count_duplicates():
    assert count_duplicates({}) == 0
    assert count_duplicates({ 'foo' : 1, 'bar' : 2, 'baz' : 3 }) == 0
    assert count_duplicates({ 'foo' : 1, 'bar' : 2, 'baz' : 1 }) == 1
    assert count_duplicates({ 'foo' : 1, 'bar' : 1, 'baz' : 1 }) == 1
    assert count_duplicates({ 'foo' : 1, 'bar' : 2, 'baz' : 3, 'bam' : 2,
                              'brr' : 1 }) == 2

if __name__ == '__main__':
    nose.runmodule()
