# AY250 Homework2 Wolfram Alpha Calculator

from types import *

def calculate(INPUT, return_float=True):

	assert type(INPUT) is StringType, "You must input a string."

	if INPUT.count('_') != 0:
		raise ValueError('Cannot evaluate input with underscores (_), it is not safe')

	try:
		OUTPUT = eval(INPUT, {})
	except Exception, e:
		print 'Python cannot evaluate, using Wolfram Alpha'		OUTPUT = 1.0 #not implemented

	if return_float == True:
		return OUTPUT
	else:
		print OUTPUT