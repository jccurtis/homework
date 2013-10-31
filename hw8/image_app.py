from matplotlib.figure import *
from enthought.traits.api import *
from enthought.traits.ui.api import *
from mpl_figure_editor import MPLFigureEditor
import matplotlib.pyplot as plt
import wx
from scipy import ndimage
import numpy as np
from image_functions import scrape_image, vignette, colorDirectionSwap

class Test(HasTraits):
    '''
    Traits GUI class for image scraping and basic processing. Excecuting 
    builds a Traits GUI object which needs to be configured to run (see
    below for if __name__ = '__main__'). The GUI allows the user to query
    the Google image search API and edit the image.
    '''
    query              = Str
    url                = Str
    runQuery           = Button
    gaussianBlur       = Button
    rotate             = Button
    fourierGaussian    = Button
    vignette           = Button
    colorDirectionSwap = Button
    imageSaveName      = Str
    imageSave          = Button
    reset              = Button 
    figure             = Instance(Figure, ())
    view = View(Item('query'),
                Item('runQuery', show_label=False),
                Item('url'),
                Item('figure', editor=MPLFigureEditor(), show_label=False),
                Item('gaussianBlur', show_label=False),
                Item('rotate', show_label=False),
                Item('fourierGaussian', show_label=False),
                Item('vignette', show_label=False),
                Item('colorDirectionSwap', show_label=False),
                Item('imageSaveName'),
                Item('imageSave', show_label=False),
                Item('reset', show_label=False),
                title = 'Google Image Search',
                buttons=['OK'],
                width=800,
                height=800,
                resizable=False)

    def __init__(self):                                          # start the gui with a temp image loaded
#        super(Test, self).__init__()
        axes = self.figure.add_subplot(111)
        self.imageSaveName = 'default_image.jpg'                 #set default image name for saving
        self.imArr = plt.imread('_placeholder_.jpeg')
        axes.imshow(self.imArr)
    def _runQuery_fired(self):                                   #image search with scrape_image from image_search.py BUTTON                     
        (url,fName,imArr) = scrape_image(self.query)
        self.imArr = imArr  #numpy image array
        self.url = url      #image url
        self.fName = fName  #downloaded filename
        self.imshow()
    def _gaussianBlur_fired(self):                               #gaussian blur BUTTON
        self.imArr = ndimage.gaussian_filter(self.imArr, 10.0)
        self.imshow()
    def _rotate_fired(self):                                     #90 deg CCW rotation BUTTON
        self.imArr = ndimage.rotate(self.imArr, 90.0)
        self.imshow()
    def _fourierGaussian_fired(self):                            #fourier gaussian transform BUTTON
        self.imArr = ndimage.fourier_gaussian(self.imArr, 2.0)
        self.imshow()
    def _vignette_fired(self):                                   #vignette BUTTON
        self.imArr = vignette(self.imArr)
        self.imshow()
    def _colorDirectionSwap_fired(self):                         #swap color and direction BUTTON
        self.imArr = colorDirectionSwap(self.imArr)
        self.imshow()
    def _imageSave_fired(self):
        plt.imsave(self.imageSaveName,self.imArr)
    def _reset_fired(self):                                      #reset to original downloaded image (only if it downloaded)
        try:
            self.imArr = plt.imread(self.fName)
            self.imshow()
        except:
            self.imArr = plt.imread('_placeholder_.jpeg')
            self.imshow()
    def imshow(self):                                             #update image
        self.figure.axes[0].images = []
        self.figure.axes[0].imshow(self.imArr)
        wx.CallAfter(self.figure.canvas.draw)

if __name__=='__main__':                                        #start gui
    c = Test()
    c.configure_traits()