# python 3.10
# Reducing uploading time in escriptorium
# usually the size of the image is about 9mb through the cropping its about 4mb
# crop each image of the folder (only 7 jpegs) and save it in another folder
from PIL import Image
import os

path = "./file/pathname/"
savepath = "./file/pathname/"
dirs = os.listdir(path)


def crop():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            imCrop = im.crop((10, 6200, 6000, 6500))  # left, upper, right, lower
            # save in other folder and rename the file to the original name with _cropped.jpg
            imCrop.save(savepath + item + '_cropped.jpg', 'JPEG', quality=100)


crop()
# thanks to the inspiration of sanjeev2552
# https://www.geeksforgeeks.org/python-pil-image-crop-method/

# next steps would be to extand the code for cropping more images,
# but the size is different
# so idea would be to add create a loop: estimate the size of the image, cropt it and go to the next image
