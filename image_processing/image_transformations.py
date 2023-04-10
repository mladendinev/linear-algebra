import numpy as np


def convolution(image_matrix, kernel, padding=0, stride=1):
    x_kernel_shape = kernel.shape[0]
    y_kernel_shape = kernel.shape[1]

    x_image_shape = image_matrix.shape[0]
    y_image_shape = image_matrix.shape[1]

    x_conv_shape = int(((x_image_shape - x_kernel_shape + 2 * padding) / stride) + 1)
    y_conv_shape = int(((y_image_shape - y_kernel_shape + 2 * padding) / stride) + 1)
    conv_output = np.zeros((x_conv_shape, y_conv_shape), dtype=np.float32)

    for column in range(y_image_shape):
        if column > y_image_shape - y_kernel_shape:
            break
        if column % stride == 0:
            for row in range(x_image_shape):
                if row > x_image_shape - x_kernel_shape:
                    break
                try:
                    if row % stride == 0:
                        conv_output[row, column] = np.sum(
                            np.multiply(
                                image_matrix[row : row + x_kernel_shape, column : column + y_kernel_shape], kernel
                            )
                        )
                except Exception as ex:
                    print("Exception occurred", ex)
                    break

    return conv_output
