#AY250 HW5

Please see notebook headers and docstrings for more details.

##Problem 1

XMLRPC Server/Client Pair for image manipulation. Three image manipulations currently implemented:

- (blur) guassian blur with kernel 0.5% of max pixel dim. Uses ndimage
- (swapColorAndDirections) moves each color channel to the next and flip left/right orientation. If greyscale, the image is only flipped left/right.
- (vignette) applies a color dodge vinette around the border of the image. Uses a mask with the magnitude of the Euclidean distance weighting each original color channel (only one if greyscale).

##Problem 2

Audio analysis class for picking out notes in tone samples. I wasn't able to complete the note picking but have generated power spectra and I dentified and marked peaks. The next step is to create a mesh of frequencies to properly pick out a note for a given frequency range.

