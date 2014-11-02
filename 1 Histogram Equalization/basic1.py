# -*- coding: utf-8 -*-

from PIL import Image # PIL(Python Imaging Library)
import matplotlib.pyplot as plt
import os

# pil_im = Image.open('flower.jpg')
pil_im = Image.open('flower.jpg').convert('LA') # for grayscale

# # Create Thumbnails
# pil_im.thumbnail((128, 128))
# # Copy Regions
# box = (100, 100, 400, 400) # (left, upper, right, lower)
# region = pil_im.crop(box)
# # Paste Regions
# region = region.transpose(Image.ROTATE_180)
# pil_im.paste(region, box)
# # Resize
# out = pil_im.resize((128, 128))
# # Rotate
# out = pil_im.rotate(45)

plt.imshow(pil_im)
# x = [100,100,400,400]
# y = [200,500,200,500]
# plt.plot(x, y, 'r*')
plt.title('Plotting')
# plt.axis('off')
plt.show()
