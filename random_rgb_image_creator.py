import numpy as np
# import matplotlib.pyplot as plt
import random
import string
import os
from skimage.io import imsave

def generate_random_name(length):
    random_name = ''.join(random.choice(string.ascii_lowercase) for _n in range(length))
    return random_name

def generate_random_image(height, width):
    random_image = np.random.rand(height, width, 3) * 255
    random_image = random_image.astype(np.uint8)
    image_name = generate_random_name(10)
    if not os.path.exists('random_rgb_image_folder'):
        os.makedirs('random_rgb_image_folder')
    imsave(f'random_rgb_image_folder/{image_name}.png', random_image)

generate_random_image(256, 256)