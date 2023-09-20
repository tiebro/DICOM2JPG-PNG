import numpy as np
import cv2
import os
import SimpleITK as sitk

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

if __name__ == '__main__':

    input_root = r'D:\DeepLearning\cervical\BianqueNet+\input\dicom'
    dir_list = os.listdir(input_root)  # 打开文件夹中的图像的文件名，作为列表返回
    output_root = r'D:\DeepLearning\cervical\BianqueNet+\input\dicom_out'
    if not os.path.exists(output_root):
        os.makedirs(output_root)
    # 开始遍历日期文件夹下的每个子文件夹
    print('The 1th class dir ' + str(input_root) + ' have ' + str(len(dir_list)) + ' files' + '*' * 50)

    for _dir in dir_list:
        try:
            if _dir != 'VERSION' and _dir != '.DS_Store':
                dir_in1_path = os.path.join(input_root, _dir)
                dir_out1_path = os.path.join(output_root, _dir)
                if not os.path.exists(dir_out1_path):
                    os.makedirs(dir_out1_path)
                dir_in2_path_list = os.listdir(dir_in1_path)
                print('The 2th class dir '+str(_dir)+' have ' + str(len(dir_in2_path_list))+' files'+'*'*50)
                # debug 使用
                j = 1
                for i in dir_in2_path_list:
                    if i != 'VERSION'and i != '.DS_Store':
                        document = os.path.join(dir_in1_path, i)
                        # countname = str(count)  # 将设置的变量数字1，转换为字符串，作为名称使用
                        countfullname = _dir + '-' +str(j) + '.jpg'
                        output_jpg_path = os.path.join(dir_out1_path, countfullname) # 设置保存每张图片的路径
                        j = j+1
                        image = sitk.ReadImage(document)
                        img_array = sitk.GetArrayFromImage(image)
                        img_array = np.squeeze(img_array, axis=0)
                        high = np.max(img_array) # 找到最大的
                        low = np.min(img_array)# 找到最小的
                        print(str(_dir)+'/'+str(i)+' have max and min pixel are:'+str(high)+' and '+str(low))
                        # 调用函数，开始转换
                        dicom2jpg(img_array, low, high, output_jpg_path)
        except Exception as e:
            print("---------------------------------------------------------the conversion of " + str(
                document) + " is failed!")
            pass
        continue
