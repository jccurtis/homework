# AY250 HW09 Multiprocessing
# Joseph Curtis

**Monte Carlo for Pi:**
![Monte Carlo Pi](http://docs.picloud.com/_images/basic_example_monte.png)


The algorithm uses a Monte Carlo dart-throwing simulation to calculate a numerical approximation to Pi. 

Write a large program that runs this algorithm under the three different parallelization methods. Run several trials with different numbers of darts thrown (up to execution times ~100 seconds). Keep track of the execution times as a function of number of darts and method of parallelization. Also, keep track of the simulation rate (darts thrown per second). If you want to be awesome (!), you can run each simulation multiple times for each number of darts and calculate the standard deviation for the execution time and the simulation rate, but this is not required.

Plot execution time and simulation rate as a function of number of darts for all three methods. If you calculated standard deviations, use errorbar plots. See the example plot on the following page and try to emulate it. In your README file, explain the behavior you measure and illustrate in the plot. The grader should be able to simply run your submitted program and reproduce the plot.


Put your plotting imports after running all the simulations. They can introduce overhead that slows down seemingly unrelated code. Do some investigation online to see examples of multiprocessing and IPython parallel.

The official python multiprocessing documentation is here:
http://docs.python.org/library/multiprocessing.html

You should investigate the pool function in particular.

You can check out IPython parallel info at these links:
http://ipython.org/ipython-doc/dev/parallel/index.html
https://github.com/minrk/PyData2012

Include your processor type in the readme (the second example plot was generated on MacBook Air with 2 GHz Intel Core i7, 2 “cores”) during explanation of measured behavior.