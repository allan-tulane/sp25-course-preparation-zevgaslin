from main import *


def test_one():
	""" done. """
	assert myfunction('Hello') == 'Hello'
	assert myfunction(1) == 1
	assert myfunction(6) == 6


def test_two():
	assert myfunction(3 + 4) == 7
