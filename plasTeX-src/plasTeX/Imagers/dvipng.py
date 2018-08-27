#!/usr/bin/env python

import plasTeX.Imagers

class DVIPNG(plasTeX.Imagers.Imager):
    """ 
    Imager that uses dvipng 
    http://www.nongnu.org/dvipng/dvipng_4.html
    -D dpi # affects the fontSize in class Dimension() in __init__.py
    -Q m # gives m*m-1 antialiasing levels  (default is 4)
    -z 0 # no compression
    """
    # command = 'dvipng -o img%d.png -D 120 -Q 4' # PlasTeX default
    # command = 'dvipng -o img%d.png -D 150 -Q 4 -z 0' # no compr., 150 dpi, set fontSize=20 inside Imagers\__init__.py 
    command = 'dvipng -o img%d.png -D 200 -Q 4 -z 0' # no compr., 200 dpi, set fontSize=26 inside Imagers\__init__.py 
    fileExtension = '.png'

    def formatConfigOptions(self, config):
        options = []
        if config['resolution']:
            options.append(('-D', config['resolution'])) 
        return options

Imager = DVIPNG
