#AY250 | HOMEWORK 4 | Joseph Curtis | October 2, 2013
---

#### General Notes:

- I had to do some clever tasks to properly extract image pixel depth because some of the images (listed below) only have a pixel channel depth of one.
- Feature extraction on a quad-core 2.2 GHz MBP takes 1178.992s about **20 minutes.**
- With my testing of training on 90% of the data and testing on 10% I got about **30% accuracy**.
- I didn't have time to finish a function (run_final_classifier) to loop through all of the files in a directory or do cross validation. I did make a feature extraction function in functions.py which can be imported. I tried to spend my time on the classifier.
- I saved the classifier (built form the full feature set) (classifier.npy), feature list (features_save.npy) and catagories (catagories_save.npy)

#### TO DO:

- Use all the images for the submission training set
- Do cross validation with subsets to test

#### Features Extracted:

1. Product of image pixel dimensions (image size)
2. Mean of Grayscale Image
3. Area of Sobel Edges Normalized By Image Size
4. Area of Sobel Edges Above 2x Mean of Sobel Edges Normalized By Image Size
5. Area of Canny Edges (Sum of booleans) Normalized By Image Size
6. Number of Harris Corners
7. Unique Felzenszwalb Image Segmentation Lines
8. Area of Vertical Sobel Edges Above 2x Mean of Sobel Edges Normalized By Image Size
9. Area of Horizontal Sobel Edges Above 2x Mean of Sobel Edges Normalized By Image Size
10. Mean of Red Channel (if grayscale: mean of the only color channel)
11. Mean of Green Channel (if grayscale: mean of the only color channel)
12. Mean of Blue Channel (if grayscale: mean of the only color channel)
13. Maximum Pixel Value of the Histogram of Oriented Gradients
14. Percent of image that is light versus dark with adaptive thresholding
15. Percent of image that is red with adaptive thresholding
16. Percent of image that is green with adaptive thresholding
17. Percent of image that is blue with adaptive thresholding
        
Scikit Image Links:

1. **SOBEL Edge Detection:** http://scikit-image.org/docs/dev/auto_examples/plot_edge_filter.html
2. **Canny Filter:** http://scikit-image.org/docs/dev/auto_examples/plot_canny.html
3. **Adaptive Filtering:** http://scikit-image.org/docs/dev/auto_examples/plot_threshold_adaptive.html
4. **Harris Corner Detection:** http://scikit-image.org/docs/dev/auto_examples/plot_corner.html
6. **Histogram of Oriented Gradients:** http://scikit-image.org/docs/dev/auto_examples/plot_hog.html
7. **Felzenszwalb’s efficient graph based segmentation:** http://scikit-image.org/docs/dev/auto_examples/plot_segmentations.html