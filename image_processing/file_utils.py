import numpy as np
from PIL import Image
import os

curr_path = os.getcwd()

def read_image_as_matrix(img):
    image = Image.open(os.path.join(curr_path, img)).resize((500, 300))
    return np.asarray(image)


def display_matrix(image_matrix):
    image = Image.fromarray(image_matrix)
    image.show()
