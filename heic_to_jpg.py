import sys
from glob import glob

import piexif
import pillow_heif
from PIL import Image
from PIL import ImageEnhance


# pillow_heif.register_heif_opener()

def heic_to_jpg(img_path, save_path):
    # open the image file
    heif_file = pillow_heif.read_heif(img_path)

    # create the new image
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data
        , "raw",
        heif_file.mode,
        heif_file.stride,
    )
    # PIL rotates the image according to exif info, so it's necessary to remove the orientation tag
    # otherwise the image will be rotated again (1° time from PIL, 2° from viewer).
    exif_dict = piexif.load(heif_file.info['exif'])
    exif_dict['0th'][274] = 0
    exif_bytes = piexif.dump(exif_dict)

    name = (img_path.split('\\')[-1]).split('.')[0]
    # 色度,增强因子为1.0是原始图像
    # 色度增强
    enh_col = ImageEnhance.Color(image)
    color = 1.2
    image_colored1 = enh_col.enhance(color)
    image_colored1.save(save_path + name + ".jpg", "JPEG", exif=exif_bytes, quality=85)  # 默认转成jpg


files = glob(r"D:/ethan/picture/print2311/*.heic")  # 读取全部heic文件地址
save_path = "D:/ethan/picture/print2311/"  # 储存地址
for img in files:
    print("Conversion process: ", img)
    sys.stdout.flush()
    heic_to_jpg(img, save_path)

print('--------------finish-------------')


# #变亮
# #亮度增强,增强因子为0.0将产生黑色图像；为1.0将保持原始图像。
# enh_bri = ImageEnhance.Brightness(image)
# brightness = 1.5
# image_brightened1 = enh_bri.enhance(brightness)
# image_brightened1.save(save_path+name+".jpg", "JPEG", exif=exif_bytes, quality=85) #默认转成jpg
#
# #变暗
# enh_bri = ImageEnhance.Brightness(image)
# brightness = 0.8
# image_brightened2 = enh_bri.enhance(brightness)
# image_brightened2.save(save_path+name+".jpg", "JPEG", exif=exif_bytes, quality=85) #默认转成jpg
#
# #色度,增强因子为1.0是原始图像
# # 色度增强
# enh_col = ImageEnhance.Color(image)
# color = 1.5
# image_colored1 = enh_col.enhance(color)
# image_colored1.save(save_path+name+".jpg", "JPEG", exif=exif_bytes, quality=85) #默认转成jpg
#
# # 色度减弱
# enh_col = ImageEnhance.Color(image)
# color = 0.8
# image_colored2 = enh_col.enhance(color)
# image_colored2.save(save_path+name+".jpg", "JPEG", exif=exif_bytes, quality=85) #默认转成jpg
#
# #对比度，增强因子为1.0是原始图片
# # 对比度增强
# enh_con = ImageEnhance.Contrast(image)
# contrast = 1.5
# image_contrasted1 = enh_con.enhance(contrast)
# image_contrasted1.save(save_path+name+".jpg", "JPEG", exif=exif_bytes, quality=85) #默认转成jpg
#
# # 对比度减弱
# enh_con = ImageEnhance.Contrast(image)
# contrast = 0.8
# image_contrasted2 = enh_con.enhance(contrast)
# image_contrasted2.save(save_path+name+".jpg", "JPEG", exif=exif_bytes, quality=85) #默认转成jpg
#
# # 锐度，增强因子为1.0是原始图片
# # 锐度增强
# enh_sha = ImageEnhance.Sharpness(image)
# sharpness = 3.0
# image_sharped1 = enh_sha.enhance(sharpness)
# image_sharped1.save(save_path+name+".jpg", "JPEG", exif=exif_bytes, quality=85) #默认转成jpg
#
# # 锐度减弱
# enh_sha = ImageEnhance.Sharpness(image)
# sharpness = 0.8
# image_sharped2 = enh_sha.enhance(sharpness)
# image_sharped2.save(save_path+name+".jpg", "JPEG", exif=exif_bytes, quality=85) #默认转成jpg
