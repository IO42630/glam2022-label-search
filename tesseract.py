import os

tesser = 'C:/Progra~1/Tesseract-OCR/tesseract'
images = 'C:/Users/User/home/ws/glam2022-label-search/data/images'
for file in os.listdir(images):
    source = images + '/' + file
    target = source.replace('images', 'text').replace('.jpg', '.txt')
    cmd = tesser + ' ' + source + ' ' + target
    os.system(command=cmd)
