# test_binsearch.py
from binsearch import binary_search
from pytest import raises
import numpy as np

# test suite

# just a simple test for checking basic functionality
def test_simple():
	assert binary_search([1,2,3], 2) == 1

# needle not in array, but within range
def test_needle_notfound_in_range():
	assert binary_search([6,9,11, 12, 13], 7) == -1

# needle not in array, but within range
def test_needle_notfound_not_in_range():
	assert binary_search([6,9,11, 12, 13], 15) == -1

# needle on left boundary
def test_needle_onleft():
	assert binary_search([0,1,2,3], 0) == 0

# needle on right boundary
def test_needle_onright():
	assert binary_search([0,1,2,3], 3) == len([0,1,2,3]) - 1

# empty list returns -1
def test_empty_list():
	assert binary_search([], 1) == -1

# nan in that gets compared array raises assertion error 
# [ this is really a precondition violation ]
def test_nan_compared_in_arr():
	assert raises(AssertionError, "binary_search([1,2, np.nan, 3], 3)")

# however this doesn't break since the nan is never compared
# against and we want to stay within our O(log(n)) performance bound.
def test_nan_nocompare_in_arr():
	assert binary_search([1,2, 3, np.nan], 3) == 2

# nan as needle raises assertion error [ this is really a precondition violation ]
def test_nan_needle():
	assert raises(AssertionError, "binary_search([1,2], np.nan)")

# `right` out of bounds
def test_right_out_of_bounds():
	assert raises(IndexError, "binary_search([1,2], 2, 0, 4)")

# `left` out of bounds
def test_left_out_of_bounds():
	assert raises(AssertionError, "binary_search([0,5], 3, -2, 4)")

# note: leaving this here because technically
# [1,2,3][1:0] == [] so this shouldn't be an error
def test_right_less_than_left():
	assert binary_search([1,2,3], 2, 1, 0) == -1

# inf is a valid needle
def test_infty():
	assert binary_search([1,2,np.inf], np.inf) == 2

# large arrays work
def test_large_array():
	assert binary_search(range(10**6), 777, 700, 800)

# testing that `2` works as needle
def test_one():
	assert binary_search([1,2,3], 1) == 0

# testing that `1` works as needle
def test_two():
	assert binary_search([1,2,3], 2) == 1

# there is no systematic way to return a value
# in case multiple are present in the array.
# what is necessary, however is that we get *A*
# return value
def test_multiple_entries():
	assert binary_search([1,1,2,3], 1) == 1