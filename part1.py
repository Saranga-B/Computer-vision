import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def reduce_intensity_levels(imageArray, numLevels):
    factor = 256 // numLevels
    reducedImage = (imageArray // factor) * factor
    return reducedImage

imagePath = "/content/image.jpg"
image = Image.open(imagePath)
imageArray = np.array(image)

numLevels = int(input("Enter the intensity levels (power of 2): "))

if numLevels & (numLevels - 1) != 0:
    print("The input should be a power of 2.")
else:
    reducedImage = reduce_intensity_levels(imageArray, numLevels)

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(imageArray, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    axes[1].imshow(reducedImage, cmap='gray')
    axes[1].set_title('Image with Reduced Intensity Levels')
    axes[1].axis('off')
    plt.show()
