# openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files

# Introduction
# openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.

# It was born from lack of existing library to read/write natively from Python the Office Open XML format.

# All kudos to the PHPExcel team as openpyxl was initially based on PHPExcel.

# Security
# By default openpyxl does not guard against quadratic blowup or billion laughs xml attacks. To guard against these attacks install defusedxml.

# Installation 
# Install openpyxl using pip. It is advisable to do this in a Python virtualenv without system packages:

# $ pip install openpyxl 

# Note: There is support for the popular lxml library which will be used if it is installed. 
# This is particular useful when creating large files.

# To be able to include images(jpeg, png, bmp, ...) into an openpyxl file, we will also need the "pillow" library that can be nstalled with
# $ pip install pillow 

