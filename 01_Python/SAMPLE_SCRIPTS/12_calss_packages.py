# Library or Package 

# Function: a named block of executable business log 
# Modules: mostly it contains similar or related multiple functions 
# Library or Package: It contains multiple Modules 
# in General modules are also related to file with .py extention 
# Package:
#	1. __init__.py : it should be the first file in the package 
#	2. modules.py : we can srote any number of module files 

"""
import sound.audio.audFormat as af
import sound.video.videoconv as vc
import sound.effects.audEffect as ae


#print(dir(sound))
print(__name__)

af.mp3()
vc.mp4()
ae.ecco()
"""

from sound.audio import *
audFormat.mp3()










