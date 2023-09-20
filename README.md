# DICOM2JPG-PNG
Today, there is an increasing amount of research focused on medical magnetic resonance imaging (MRI). However, collecting original patient MRI image BMP files from various hospitals is very challenging for various reasons. In comparison, collecting patients' original DICOM files is easier than MR files. Therefore, we propose using Python to implement batch conversion of DICOM files into jpg or png images.

1.Installing Modules
pip install numpy
pip install cv2
pip install simpleitk
pip install os

2.Define a function for DICOM to JPG conversion
The function reads pixel value information of the image, converts it to an array format, and after normalization, converts it to a three-channel RGB image.
# 定义dicom to jpg转换函数
def dicom2jpg(img, low_window, high_window, save_path):
    """
    :param img: dicom图像的像素值信息
    :param low_window: dicom图像像素值的最低值
    :param high_window: dicom图像像素值的最高值
    :param save_path: 新生成的jpg图片的保存路径
    :return:
    """
    oldimg = np.array([low_window * 1., high_window * 1.]) # 将像素值转换为array
    newimg = (img - oldimg[0]) / (oldimg[1] - oldimg[0]) # 将像素值归一化0-1
    newimg = (newimg * 255).astype('uint8') # 再转换至0-255，且将编码方式由原来的unit16转换为unit8
    # 将单通道转换成三通道
    img_out = np.zeros([newimg.shape[0], newimg.shape[1], 3])
    img_out[:, :, 0] = newimg
    img_out[:, :, 1] = newimg
    img_out[:, :, 2] = newimg
    # 用cv2写入图像指令，保存jpg即可
    cv2.imwrite(save_path, img_out, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
