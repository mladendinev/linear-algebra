from file_utils import read_image_as_matrix, display_matrix
from image_transformations import convolution
import numpy as np


if __name__ == "__main__":
    image_matrix = read_image_as_matrix(
        "pexels-photo-458976.jpeg"
    )
    display_matrix(image_matrix)
    # kernel = np.array([[0, -1, 0], [-0, 4, -1], [0, -1, 0]])
    # kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    # kernel = np.array([[0, 1, 0], [1, 1.5, 1], [0, 1, 0]])
    kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    convoluted_image = convolution(image_matrix, kernel=kernel)
    # display_matrix(convoluted_image)
