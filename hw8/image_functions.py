import os
import urllib
import urllib2
import sys
import time
import simplejson
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

def scrape_image(query):
    '''
    Input:  query - string passed to Google image search Ajax api. 
                    Google returns 8 image results in JSON format
                    with url's and other information. The unescapedUrl
                    is used to attempt to download the images starting 
                    with the first one. If the image is not successfully 
                    downloaded, the next image is attempted and so on.
                    It is expected that in the 8 responses returned, at 
                    least one of the images will successfully download
                    and not be a broken link.
    
    Outputs:     url   - string of scraped image url
                 fName - filename of scraped and SAVED image
                 imArr - numpy array of image
    '''
    # Format url and pull raw web JSON code
    urlQuery = 'https://ajax.googleapis.com/ajax/services/search/images?' + \
                urllib.urlencode(OrderedDict([('q',query),
                                              ('as_filetype','jpg'),
                                              ('v','1.0'),
                                              ('rsz','8')]))
    #request = urllib2.Request(urlQuery, None, {'Referer': 'testing'})
    response = urllib2.urlopen(urlQuery)
    # Get results using JSON each item contains one response
    results = simplejson.load(response)['responseData']['results']
    # Save first image with a check to make sure the image downloads correctly (unlikely that 8 images wouldn't work)
    fName = query+'.jpg'
    counter = 0
    for result in results:
        url = result['unescapedUrl']
        counter += 1
        try:
            urllib.urlretrieve(url,fName)
            break
        except:
            print counter,"image(s) didn't download correctly"
    # Load the image
    imArr = plt.imread(fName)
    return url,fName,imArr

def vignette(imArr):
    '''
    Performs vignetting to the image using a mask (with the center bright) 
    for pixel burning using the magnitude of the Euclidian distance from 
    the center of the image as the mask value. The mask is then normalized
    and multiplied by each color channel (only one if greyscale).
    
    Input:  imArr - Numpy image array
    
    Output: imArrMasked - imArr with vignetting
    '''
    pxHeight = imArr.shape[0]
    pxWidth  = imArr.shape[1]
    pxDepth  = len(imArr.shape)   #1 for grayscale, 3 for RGB
    #center of image pixel array
    pxHeightHalf = pxHeight/2
    pxWidthHalf = pxWidth/2
    #build mask (center dark) for pixel burning using the magnitude of 
    #Euclidian distance from the center of the image. I had to be 
    #careful of data types here becuase I got overflow with int8's.
    #Thus I set the Mask dtype to float.
    imMask = np.zeros_like(imArr, dtype=np.float)
    for y in range(pxHeight):
        for x in range(pxWidth):
            px = np.sqrt((pxHeightHalf-y)**2+(pxWidthHalf-x)**2)
            if pxDepth == 3:
                imMask[y,x,0] = px
                imMask[y,x,1] = px
                imMask[y,x,2] = px
            else:
                imMask[y,x] = px
    #inverse mask (center bright) and normalize
    imMaskNorm = 1-imMask/imMask.max()
    imArrMasked = imArr.copy()
    #apply mask to every layer
    if pxDepth == 3:
        for i in range(3):
            imArrMasked[...,i] = imArr[...,i]*imMaskNorm[...,i]
    else:
        imArrMasked = imArr*imMaskNorm
    return imArrMasked

def colorDirectionSwap(imArr):
    '''
    Shifts each color channel to the next one:
        Red   -> Green
        Green -> Blue
        Blue  -> Red
    Flips the image on the x axis (left/right).
    
    NOTE: If the image is greyscale, only the x axis is flipped 
    since there are no color channels to swap.
    
    Input: imArr - numpy image array of 1 or 3 bit depth
    
    Output: imArr - numpy image array with color channels and left right directions swapped
    '''
    if len(imArr.shape) == 3:
        imTemp = np.zeros_like(imArr)
        imTemp[...,1] = imArr[...,0] #R -> G
        imTemp[...,2] = imArr[...,1] #G -> B
        imTemp[...,0] = imArr[...,2] #B -> R
        imArr         = imTemp[:,::-1,:] #flip left right
    elif len(self._imShape_) == 2:
        imArr = imArr[:,::-1] #flip left right
    else:
        raise ValueError('Image array is not shaped correctly.')
    return imArr