
import os
import urllib
import urllib2
import sys
import time
import simplejson
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

def scrapeImage(query):
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
                 fName - filename of scraped image
                 imArr - numpy array of image
    '''
    # Format url and pull raw web JSON code
    urlQuery = 'https://ajax.googleapis.com/ajax/services/search/images?' + \
                urllib.urlencode(OrderedDict([('q',query),
                                              ('imgsz','medium'),
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
            urllib.urlretrieve(url,'test.jpg')
            break
        except:
            print counter,"image(s) didn't download correctly"
    # Load the image
    imArr = plt.imread(fName)
    return url,fName,imArr