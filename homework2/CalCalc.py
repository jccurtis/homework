# AY250 Homework2 Wolfram Alpha Calculator

from types import StringType
import urllib2
from xml.etree.ElementTree import fromstring
import argparse

def calculate(INPUT, return_float=False, use_wolf=False):

	assert type(INPUT) is StringType, "You must input a string."

	if INPUT.count('_') != 0:
		raise ValueError('Cannot evaluate input with underscores (_), it is not safe')

	try:
		if use_wolf==True:
			raise ValueError('User wants to evaluate with Wolfram Alpha')
		OUTPUT = eval(INPUT, {})
	except Exception, e:
		print 'Python cannot evaluate, using Wolfram Alpha...'
		URL = 'http://api.wolframalpha.com/v2/query?input=' + INPUT.replace(' ', '%20') + '&appid=UAGAWR-3X6Y8W777Q'
		print 'URL: ' + URL
		response = urllib2.urlopen(URL)               #xml code from wolfram alpha
		parsed_response = fromstring(response.read()) #convert xml to tree structure
		OUTPUT = parsed_response[1][0][0].text        #takes the value of the 2nd child, 1st subchild, 1st subsubchild

	if return_float == True:
		return OUTPUT
	else:
		print OUTPUT

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Wolfram Alpha String Calculator')
	parser.add_argument('INPUT', help='Input a string')
	parser.add_argument('-w', action='store_true', default=False, dest='boolean_switch', help='Boolean switch to force Wolfram Usage')
	results = parser.parse_args()

	calculate(results.INPUT,False,results.boolean_switch)
