# from django.db import models
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt


# def testMethodFromModelPY(path=''):
  
#         img = Image.open("maxWallpaper.jpg")

#         image_array = np.array(img)
#         size = 0


#         positionx = np.random.randint(100,1900)
#         positiony = np.random.randint(100,900)
            
#         image_array[:,positionx-size:positionx+size,:] = [225,0,0] 
#         image_array[positiony-size:positiony+size,:,:] = [0,255,0] 
#         plt.imshow(image_array)
            

#         plt.show() 
# import matplotlib.pyplot as plt
# from PIL import Image
# import numpy as np

# imagen = Image.open("maxWallpaper.jpg")

# imagen_array = np.array(imagen)

# # Definir el ruido tipo speckle
# noise = np.random.normal(0, 0.5, size=imagen_array.shape)

# # Agregar el ruido a la imagen
# noisy_image = imagen_array + imagen_array * noise
# # noisy_image = imagen_array

# # Definir el kernel del filtro promediador
# kernel_size = 12
# #Filtro promediador
# kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)

# def testMethodFromModelPY(path=''):
    

#     # quantity = np.random.randint(2,8)

#     # for i in range(quantity):
#     #     size = np.random.randint(0,100)
#     #     positionx = np.random.randint(100,1900)
#     #     positiony = np.random.randint(100,900)
#     #     colors = np.random.randint(100,255)
#     #     image_array[:,positionx-size:positionx+size,:] = [colors,0,0] 
#     #     image_array[positiony-size:positiony+size,:,:] = [0,colors,0] 


#     smoothed_image = np.zeros_like(noisy_image)
#     for channel in range(imagen_array.shape[2]):
#         for row in range(noisy_image.shape[0] - kernel_size + 1):
#             for col in range(noisy_image.shape[1] - kernel_size + 1):
#                 # Obtener la submatriz para el canal actual
#                 subMatrix = noisy_image[row:row+kernel_size, col:col+kernel_size, channel]
#                 # Aplicar el filtro promediador
#                 smoothed_image[row + 1, col + 1, channel] = np.sum(subMatrix * kernel)

#     fig, ax = plt.subplots()
#     ax.imshow(noisy_image.astype(np.uint8))
#     ax.axis('off')  # Hide axes
#     return fig



import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
imagen = Image.open("maxWallpaper.jpg")
image_array = np.array(imagen)
    
def apply_filter(noisy_image, kernel):
    smoothed_image = np.zeros_like(image_array)
    for channel in range(image_array.shape[2]):
        for row in range(image_array.shape[0] - kernel.shape[0] + 1):
            for col in range(image_array.shape[1] - kernel.shape[1] + 1):
                sub_matrix = noisy_image[row:row+kernel.shape[0], col:col+kernel.shape[1], channel]
                smoothed_image[row + 1, col + 1, channel] = np.sum(sub_matrix * kernel)
    fig, ax = plt.subplots()
    ax.imshow(smoothed_image.astype(np.uint8))
    ax.axis('off')
    return fig

def default_image():
    # Load image
    
    fig, ax = plt.subplots()
    ax.imshow(image_array.astype(np.uint8))
    ax.axis('off')  # Hide axes
    return fig

def suavizado1():
    kernel_size = 12
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    noise = np.random.normal(0, 10, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    
    return apply_filter(noisy_image, kernel)

def ruido1():
    kernel = np.array([
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ])
    return apply_filter(image_array, kernel)

def ruido2():
    kernel = np.ones((3, 3)) 
    kernel[1:-1, 1:-1] = 0.1
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido3():
    kernel = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])
    noise = np.random.normal(0, 0.005, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido4():
    kernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ])
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido5():
    kernel = np.array([
        [-5, -4, 1],
        [-2, 2, 5],
        [2, 4, 7]
    ])
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido6():
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

def ruido7():
    kernel = np.array([
        [-1, -1, 0],
        [-1, 2, 1],
        [0, 1, 1]
    ])
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)

def ruido8():
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

def ruido9():
    kernel = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])
    noise = np.random.normal(0, 0.01, size=image_array.shape)
    noisy_image = image_array + image_array * noise
    return apply_filter(noisy_image, kernel)
# def testMethodFromModelPY2(path=''):
    

#     # quantity = np.random.randint(2,8)

#     # for i in range(quantity):
#     #     size = np.random.randint(0,100)
#     #     positionx = np.random.randint(100,1900)
#     #     positiony = np.random.randint(100,900)
#     #     colors = np.random.randint(100,255)
#     #     image_array[:,positionx-size:positionx+size,:] = [colors,0,0] 
#     #     image_array[positiony-size:positiony+size,:,:] = [0,colors,0] 


#     for row in range(0,img_rowSize-kernel_rowSize+1):
#         for col in range(0,img_colSize-kernel_colSize+1):
#             subMatrix = img[row:row+kernel_rowSize, 
#                             col:col+kernel_colSize]
#             temp = subMatrix * kernel
#             res[row + matrix_pivot, col + matrix_pivot] = np.sum(temp)
            

#     fig, ax = plt.subplots()
#     plt.subplot(1,2,1)
#     ax.imshow(image_array,cmap="Greens")

#     plt.subplot(1,2,2)
#     ax.imshow(image_array, cmap="gray")
#     (image_array)
#     ax.axis('off')  # Hide axes
#     return fig