import sys
from datetime import datetime
from glob import glob

import piexif
from PIL import Image, ExifTags
from pillow_heif import register_heif_opener

register_heif_opener()


# Convert files to jpg while keeping the timestamp
def heic_to_jpg(img_path, save_path):
    image = Image.open(img_path)
    image_exif = image.getexif()
    if image_exif:
        # Make a map with tag names and grab the datetime
        exif = {ExifTags.TAGS[k]: v for k, v in image_exif.items() if k in ExifTags.TAGS and type(v) is not bytes}
        date = datetime.strptime(exif['DateTime'], '%Y:%m:%d %H:%M:%S')

        # Load exif data via piexif
        exif_dict = piexif.load(image.info["exif"])

        # Update exif data with orientation and datetime
        exif_dict["0th"][piexif.ImageIFD.DateTime] = date.strftime("%Y:%m:%d %H:%M:%S")
        exif_dict["0th"][piexif.ImageIFD.Orientation] = 1
        exif_bytes = piexif.dump(exif_dict)

        # Save image as jpeg
        name = (img_path.split('\\')[-1]).split('.')[0]
        image.save(save_path + name + ".jpg", "jpeg", exif=exif_bytes)
    else:
        print(f"Unable to get exif data for {img_path}")


files = glob(r"D:/ethan/picture/print2311/*.heic")  # 读取全部heic文件地址
save_path = "D:/ethan/picture/print2311/"  # 储存地址
for img in files:
    print("Conversion process: ", img)
    sys.stdout.flush()
    heic_to_jpg(img, save_path)

print('--------------finish-------------')
