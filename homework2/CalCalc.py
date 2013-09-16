# AY250 Homework2 Wolfram Alpha Calculator

from types import *

def calculate(INPUT):

	assert type(INPUT) is StringType, "You must input a string."

	try:
		return eval(INPUT)
	except Exception, e:
		print 'Python cannot evaluate, using Wolfram Alpha'