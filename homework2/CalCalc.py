# AY250 Homework2 Wolfram Alpha Calculator

def calculate(INPUT):

	try:
		return eval(INPUT)
	except Exception, e:
		print 'Python cannot evaluate, using Wolfram Alpha'