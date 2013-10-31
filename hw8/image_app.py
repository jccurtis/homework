from matplotlib.figure import *
from enthought.traits.api import *
from enthought.traits.ui.api import *
from mpl_figure_editor import MPLFigureEditor
import matplotlib.pyplot as plt
import wx
import scipy.ndimage as imgproc
import numpy as np
from image_functions import scrape_image, vignette

class Test(HasTraits):
    query = Str
    run_query = Button
    gaussian_filter = Button
    rotate = Button
    fourier_gaussian = Button
    vignette = Button
    url = Str
    figure = Instance(Figure, ())
    curimage = None
    view = View(Item('query'),
                Item('run_query'),
                Item('url'),
                Item('gaussian_filter'),
                Item('rotate'),
                Item('fourier_gaussian'),
                Item('vignette'),
                Item('figure', editor=MPLFigureEditor(), show_label=False),
                title = 'Google Image Search',
                buttons=['OK'],
                width=1000,
                height=1000,
                resizable=False)
    def __init__(self):                                           # start the gui with a temp image loaded
#        super(Test, self).__init__()
        axes = self.figure.add_subplot(111)
        axes.imshow(plt.imread('placeholder.jpeg'))
    def _run_query_fired(self):                                   #image search with scrape_image from image_search.py BUTTON                     
        (url,fName,imArr) = scrape_image(self.query)
        self.im = imArr
        self.url = url
        self.imshow()
    def _gaussian_filter_fired(self):                             #gaussian blur BUTTON
        self.im = imgproc.filters.gaussian_filter(self.im, 2.0)
        self.imshow()
    def _rotate_fired(self):                                      #90 deg CCW rotation BUTTON
        self.im = imgproc.interpolation.rotate(self.im, 90.0)
        self.imshow()
    def _fourier_gaussian_fired(self):                            #fourier transform BUTTON
        self.im = imgproc.fourier.fourier_gaussian(self.im, 2.0)
        self.imshow()
    def _vignette_fired(self):
        self.im = vignette(self.im)
        self.imshow()
    def imshow(self):                                             #update image
        self.figure.axes[0].images = []
        self.figure.axes[0].imshow(self.im)
        wx.CallAfter(self.figure.canvas.draw)
  
# run everything
c = Test()
c.configure_traits()