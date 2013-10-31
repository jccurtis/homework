#AY250 HW8 - GUI's

To start the GUI from within `ipython`:

	run image_app.py

**Note about Enthought Usage:** Due to the OSX update this assignment became rather problematic for implementation of traits through anaconda (I didn't have wxPython setup beforehand.) Thus I decided to use my parallel installation of Enthought's Canopy which comes preloaded with all the necessary packages for my code. The code is setup to use both anaconda and canopy (with try except) but I haven't tested with anaconda because I couldn't get wxPython working.

## GUI Closing Bug

The GUI won't close correctly with the close window `X` or with the `OK` button. I could not fix this bug. Upon the first execution of the script, the `OK` button will properly kill the process but the window remains and is **NOT** closable. Upon a second execution, errors begin to be thrown... I didn't have a chance to fix this with a `Handler` class (see links below) but from what I understand it should not have been happening to begin with. It is most likely linked to the mpl_figure_editor.py hack which is implemented to get the mpl figure as a trait.

http://code.enthought.com/projects/files/ets_api/enthought.traits.ui.handler.Handler.html
http://code.enthought.com/projects/traits/docs/html/TUIUG/handler.html
http://stackoverflow.com/questions/11036985/close-traitsui-window-without-clicking-ok

## mpl_figure_editor.py

I pulled this code from [enthought's website](http://code.enthought.com/projects/traits/docs/html/tutorials/traits_ui_scientific_app.html). It allows me to link the mpl figure to a traits HasAttributes framework. It requires the pylab or matplotlib backend to be `wx`.

## Google image search through AJAX:

The Main [article](http://stackoverflow.com/questions/11242967/python-search-with-image-google-images) I followed from Stackoverflow got me started on building a funcion to scrape the first functioning image from Google. The [Google documentation](https://developers.google.com/image-search/v1/jsondevguide#json_args) helped with the URL arguments. I ran into some issues with dead image links which I accounted for with a loop over the 8 (max allowed) returned results until one can be succesfully downloaded. I only download jpgs to avoid unforeseen issue with image processing.

## Image manipulation:

I added a variety of different image manipulations, some from [scipy.ndimage](http://scipy-lectures.github.io/advanced/image_processing/) and others from my own code from hw5.

## Image Handling:

The code saves the downloaded images to `downloaded_images` and user saved images to `saved_images`. These image saves allow the user to reset the image to a non-modified state. There is not currently an image cleanup script...

## Future work:

- Fix GUI closing issue.
- Clean up GUI elements.
- Clean up downloaded images upon exit (couldn't get working because I couldn't exit properly).
- Add multi image download functionality
- Get image processing buttons next to each other.
- Better error handling if no image found.

## Other resources:

http://stackoverflow.com/questions/3042757/downloading-a-picture-via-urllib-and-python
http://wiki.scipy.org/Cookbook/EmbeddingInTraitsGUI
http://stackoverflow.com/questions/477573/easy-install-of-wxpython-has-setup-script-error/478200#478200
http://docs.enthought.com/chaco/user_manual/chaco_tutorial.html