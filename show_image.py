'''open a image via image viewer '''

import sys
import subprocess

def openImage(path):
    imageViewerFromCommandLine = {'linux':'eog',
                                  'win32':'explorer',
                                  'darwin':'open'}[sys.platform]
    subprocess.run([imageViewerFromCommandLine, path])

openImage('1.jpg')    