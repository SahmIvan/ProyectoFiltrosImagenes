# import matplotlib.pyplot as plt
# from PIL import Image
# import numpy as np
# imagen = Image.open("maxWallpaper.jpg")
# image_array = np.array(imagen)
    
# def apply_filter(noisy_image, kernel):
#     smoothed_image = np.zeros_like(image_array)
#     for channel in range(image_array.shape[2]):
#         for row in range(image_array.shape[0] - kernel.shape[0] + 1):
#             for col in range(image_array.shape[1] - kernel.shape[1] + 1):
#                 sub_matrix = noisy_image[row:row+kernel.shape[0], col:col+kernel.shape[1], channel]
#                 smoothed_image[row + 1, col + 1, channel] = np.sum(sub_matrix * kernel)
#     fig, ax = plt.subplots()
#     ax.imshow(smoothed_image.astype(np.uint8))
#     ax.axis('off')
#     return fig

# def default_image():
#     # Load image
    
#     fig, ax = plt.subplots()
#     ax.imshow(image_array.astype(np.uint8))
#     ax.axis('off')  # Hide axes
#     return fig

# def suavizado1():
#     kernel_size = 12
#     kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
#     noise = np.random.normal(0, 10, size=image_array.shape)
#     noisy_image = image_array + image_array * noise
    
#     return apply_filter(noisy_image, kernel)

# def ruido1():
#     kernel = np.array([
#         [-2, -1, 0],
#         [-1, 1, 1],
#         [0, 1, 2]
#     ])
#     return apply_filter(image_array, kernel)

# def ruido2():
#     kernel = np.ones((3, 3)) 
#     kernel[1:-1, 1:-1] = 0.1
#     noise = np.random.normal(0, 0.01, size=image_array.shape)
#     noisy_image = image_array + image_array * noise
#     return apply_filter(noisy_image, kernel)

# def ruido3():
#     kernel = np.array([
#         [-1, -2, -1],
#         [0, 0, 0],
#         [1, 2, 1]
#     ])
#     noise_level = 0.00005
#     noise = np.full_like(image_array, noise_level)
#     noisy_image = image_array + image_array * noise
#     return apply_filter(noisy_image, kernel)

# def ruido4():
#     kernel = np.array([
#         [-1, -1, -1],
#         [-1, 9, -1],
#         [-1, -1, -1]
#     ])
#     noise = np.random.normal(0, 0.01, size=image_array.shape)
#     noisy_image = image_array + image_array * noise
#     return apply_filter(noisy_image, kernel)

# def ruido5():
#     kernel = np.array([
#         [-5, -4, 1],
#         [-2, 2, 5],
#         [2, 4, 7]
#     ])
#     noise = np.random.normal(0, 0.01, size=image_array.shape)
#     noisy_image = image_array + image_array * noise
#     return apply_filter(noisy_image, kernel)

# def ruido6():
#     kernel = np.array([
#         [-1, -1, -1, -1, -1],
#         [-1, -1, -1, -1, -1],
#         [-1, -1, 25, -1, -1],
#         [-1, -1, -1, -1, -1],
#         [-1, -1, -1, -1, -1]
#     ]) / 9
#     noise = np.random.normal(0, 0.01, size=image_array.shape)
#     noisy_image = image_array + image_array * noise
#     return apply_filter(noisy_image, kernel)

# def ruido7():
#     kernel = np.array([
#         [-1, -1, 0],
#         [-1, 2, 1],
#         [0, 1, 1]
#     ])
#     noise = np.random.normal(0, 0.01, size=image_array.shape)
#     noisy_image = image_array + image_array * noise
#     return apply_filter(noisy_image, kernel)

# def ruido8():
#     kernel = np.array([
#         [-1, -2, -1, -1, -1],
#         [-1, -2, -1, -1, -1],
#         [-1, -2, -1, -1, -1],
#         [-1, -2, -1, -1, -1],
#         [-1, -2, -1, -1, -1]
#     ])
#     noise = np.random.normal(0, 0.01, size=image_array.shape)
#     noisy_image = image_array + image_array * noise
#     return apply_filter(noisy_image, kernel)

# def ruido9():
#     kernel = np.array([
#         [1, 1, 1],
#         [1, 1, 1],
#         [1, 1, 1]
#     ])
#     noise = np.random.normal(0, 0.01, size=image_array.shape)
#     noisy_image = image_array + image_array * noise
#     return apply_filter(noisy_image, kernel)


import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
    
def apply_filter(noisy_image, kernel):
    smoothed_image = np.zeros_like(noisy_image)
    for channel in range(noisy_image.shape[2]):
        for row in range(noisy_image.shape[0] - kernel.shape[0] + 1):
            for col in range(noisy_image.shape[1] - kernel.shape[1] + 1):
                sub_matrix = noisy_image[row:row + kernel.shape[0], col:col + kernel.shape[1], channel]
                smoothed_image[row + 1, col + 1, channel] = np.sum(sub_matrix * kernel)
    fig, ax = plt.subplots()
    ax.imshow(smoothed_image.astype(np.uint8))
    ax.axis('off')
    return fig


def default_image(image_array):
    # Load image
    fig, ax = plt.subplots()
    ax.imshow(image_array.astype(np.uint8))
    ax.axis('off')  # Hide axes
    return fig

def suavizado1(image_array):
    kernel_size = 12
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    noise = np.random.normal(0, 10, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    
    return apply_filter(noisy_image, kernel)

def ruido1(image_array):
    kernel = np.array([
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ])
    return apply_filter(image_array, kernel)

def ruido2(image_array):
    kernel = np.ones((3, 3)) 
    kernel[1:-1, 1:-1] = 0.1
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido3(image_array):
    kernel = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])
    noise = np.random.normal(0, 0.005, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido4(image_array):
    kernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ])
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido5(image_array):
    kernel = np.array([
        [-5, -4, 1],
        [-2, 2, 5],
        [2, 4, 7]
    ])
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido6(image_array):
    kernel = np.array([
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, 25, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1]
    ]) / 9
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido7(image_array):
    kernel = np.array([
        [-1, -1, 0],
        [-1, 2, 1],
        [0, 1, 1]
    ])
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido8(image_array):
    kernel = np.array([
        [-1, -2, -1, -1, -1],
        [-1, -2, -1, -1, -1],
        [-1, -2, -1, -1, -1],
        [-1, -2, -1, -1, -1],
        [-1, -2, -1, -1, -1]
    ])
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido9(image_array):
    kernel = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)