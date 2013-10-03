from os import listdir
from multiprocessing import Pool, cpu_count
from pylab import imread
from time import time
import skimage as skim
from skimage import filter, feature, util, segmentation
import numpy as np

MYDIRECTORY = "/Users/josephcurtis/python/ay250/homework/hw4/50_categories"

# Quick function to divide up a large list into multiple small lists, 
# attempting to keep them all the same size. Author: Christopher Klein, Joshua Bloom
def split_seq(seq, size):
        newseq = []
        splitsize = 1.0/size*len(seq)
        for i in range(size):
            newseq.append(seq[int(round(i*splitsize)):
                int(round((i+1)*splitsize))])
        return newseq

# FEATURE EXTRACTION
def extract_features(im_cat_path_list):
    '''
    Extract Features takes a list of 2 element lists:
        
        [catagory of image , path to image]
    
    and extracts 15 features from this image. The output is a list of 3 element lists:
    
        [catagory of image , path to image, [list of features]]
        
    The 15 features are:
        
        1     Product of image pixel dimensions (image size)
        2     Mean of Grayscale Image
        3     Area of Sobel Edges Normalized By Image Size
        4     Area of Sobel Edges Above 2x Mean of Sobel Edges Normalized By Image Size
        5     Area of Canny Edges (Sum of booleans) Normalized By Image Size
        6     Number of Harris Corners
        7     Unique Felzenszwalb Image Segmentation Lines
        8     Area of Vertical Sobel Edges Above 2x Mean of Sobel Edges Normalized By Image Size
        9     Area of Horizontal Sobel Edges Above 2x Mean of Sobel Edges Normalized By Image Size
        10-12 Mean of Red/Green/Blue Channels (if grayscale: mean of the only color channel)
        13    Maximum Pixel Value of the Histogram of Oriented Gradients
        14    Percent of image that is light versus dark with adaptive thresholding
        15-17 Percent of image that is red/green/blue with adaptive thresholding
    '''

    cat_path_features = []
    
    for im_cat, im_path in im_cat_path_list:
        
        #RAW IMAGE
        im_raw = imread(im_path) #image matrix
        
        #RAW IMAGE FLATTENED IF NOT ALREADY FLAT
        if len(np.shape(im_raw)) == 3:
            im_raw_flat = np.median(im_raw, axis=2)
        else:
            im_raw_flat = im_raw    
        
        #Size of image
        im_y = float(im_raw.shape[0])
        im_x = float(im_raw.shape[1])
        im_size = im_y*im_x
        
        #LIST OF FEATURES
        features = []
        
        #FEATURE 1: Product of image pixel dimensions (image size)
        features.append(float(im_size))
        
        #FEATURE 2: Mean of Grayscale Image
        features.append(im_raw_flat.mean())
        
        #FEATURE 3: Area of Sobel Edges Normalized By Image Size
        im_edge_sobel = filter.sobel(im_raw_flat)
        features.append(im_edge_sobel.sum()/im_size)
        
        #FEATURE 4: Area of Sobel Edges Above 2x Mean of Sobel Edges Normalized By Image Size
        features.append(float((im_edge_sobel > im_edge_sobel.mean()*2).sum())/im_size)
        
        #FEATURE 5: Area of Canny Edges (Sum of booleans) Normalized By Image Size
        im_canny = filter.canny(im_raw_flat, sigma=8)
        features.append(im_canny.sum().astype(float)/im_size)
        
        #FEATURE 6: Number of Harris Corners
        im_corners = feature.corner_peaks(feature.corner_harris(im_raw_flat), min_distance=5)
        features.append(float(len(im_corners)))
        
        #FEATURE 7: Unique Felzenszwalb Image Segmentation Lines
        im_raw_float = util.img_as_float(im_raw[::2, ::2])
        im_felzen_segments = segmentation.felzenszwalb(im_raw_float, scale=100, sigma=0.5, min_size=50)
        features.append(float(len(np.unique(im_felzen_segments))))
        
        #FEATURE 8: Area of Vertical Sobel Edges Above 2x Mean of Sobel Edges Normalized By Image Size
        im_edge_vsobel = filter.vsobel(im_raw_flat)
        features.append(float((im_edge_vsobel > im_edge_vsobel.mean()*2).sum())/im_size)
        
        #FEATURE 9: Area of Horizontal Sobel Edges Above 2x Mean of Sobel Edges Normalized By Image Size
        im_edge_hsobel = filter.hsobel(im_raw_flat)
        features.append(float((im_edge_hsobel > im_edge_hsobel.mean()*2).sum())/im_size)
        
        #FEATURE 10-12: Mean of Red/Green/Blue Channels (if grayscale: mean of the only color channel)
        if len(np.shape(im_raw)) == 3:
            features.append(im_raw[...,0].mean())
            features.append(im_raw[...,1].mean())
            features.append(im_raw[...,2].mean())
        else:
            features.append(im_raw_flat.mean())
            features.append(im_raw_flat.mean())
            features.append(im_raw_flat.mean())
        
        #FEATURE 13: Maximum Pixel Value of the Histogram of Oriented Gradients
        im_fd, im_hog = feature.hog(im_raw_flat, orientations=8, pixels_per_cell=(16 , 16), cells_per_block=(1, 1), visualise=True)
        features.append(im_hog.max())
        
        #FEATURE 14: Percent of image that is light versus dark with adaptive thresholding
        im_thres_flat = filter.threshold_adaptive(im_raw_flat, 100 , 'mean')
        features.append(im_thres_flat.sum()/im_size)
        
        #FEATURE 15-17: Percent of image that is red/green/blue with adaptive thresholding
        im_thres_red = filter.threshold_adaptive(im_raw[...,0], 100 , 'mean')
        im_thres_green = filter.threshold_adaptive(im_raw[...,1], 100 , 'mean')
        im_thres_blue = filter.threshold_adaptive(im_raw[...,2], 100 , 'mean')
        features.append(im_thres_red.sum()/im_size)
        features.append(im_thres_green.sum()/im_size)
        features.append(im_thres_blue.sum()/im_size)
        
        #BUILD OUTPUT LIST FOR THIS IMAGE
        cat_path_features.append([im_cat, im_path, features])
        
        #CLEAR IMAGE PROC DATA
        del im_raw
        del im_raw_flat
        del im_raw_float
        del im_edge_sobel
        del im_canny
        del im_corners
        del im_felzen_segments
        del im_edge_vsobel
        del im_edge_hsobel
        del im_fd
        del im_hog
        
    return cat_path_features