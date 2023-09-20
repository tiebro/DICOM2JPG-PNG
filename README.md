# DICOM2JPG-PNG
Today, there is an increasing amount of research focused on medical magnetic resonance imaging (MRI). However, collecting original patient MRI image BMP files from various hospitals is very challenging for various reasons. In comparison, collecting patients' original DICOM files is easier than MR files. Therefore, we propose using Python to implement batch conversion of DICOM files into jpg or png images.

1.Installing Modules
pip install numpy
pip install cv2
pip install simpleitk
pip install os

2.Define a function for DICOM to JPG conversion
The function reads pixel value information of the image, converts it to an array format, and after normalization, converts it to a three-channel RGB image.

