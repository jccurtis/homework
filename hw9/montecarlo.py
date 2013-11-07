from random import uniform
from math import sqrt
from time import time
import numpy as np


def dartSplit(n,nnodes):
	'''
	Breaks n darts into a nnodes length list of darts 
	for each core. Each number of darts of output
	n_scatter is equal or nearly equal (with n mod nnodes 
	given to the first core. Since this modulus is likely 
	to be less than 6 (hex core) adding the entire modulus
	to the first core is not considered to lengthen the 
	process for that core.
	'''
	n_scatter = [np.floor(n/nnodes)+n%nnodes]+[np.floor(n/nnodes)]*(nnodes-1)
	return n_scatter

def darts(numDarts):
	'''
	'''
	numDarts = int(numDarts)                     #convert input to int
	circleDarts = 0                              #counter for darts in circle
	start = time()                               #start time
	for n in xrange(numDarts):                   #circle centered at 
		x, y = uniform(0,1), uniform(0,1)        #(0.5,0.5), random
		if sqrt((x-0.5)**2+(y-0.5)**2) <= 0.5:   #darts sampled in unit
			circleDarts += 1                     #square, counted in circ
	end = time()                                 #end time
	piApprox = 4*circleDarts/float(numDarts)     #extract pi from mc run
	execTime = end-start                         #execution time
	dartsPerSec = numDarts/float(execTime)       #darts thrown per sec
	return piApprox,circleDarts,numDarts,execTime,dartsPerSec