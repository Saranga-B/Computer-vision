import cv2
import numpy as np
import matplotlib.pyplot as plt

def averageFilter(image, kernelSize):
    return cv2.blur(image, (kernelSize, kernelSize))

imagePath = "/content/image.jpg"
image = cv2.imread(imagePath)

if image is None:
    print("Error: Unable to load image.")
else:
    #display
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))

    axes[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')

    for i, kernelSize in enumerate([3, 10, 20]):
        row = (i + 1) // 2
        col = (i + 1) % 2
        filteredImage = averageFilter(image, kernelSize)
        axes[row, col].imshow(cv2.cvtColor(filteredImage, cv2.COLOR_BGR2RGB))
        axes[row, col].set_title(f' ( {kernelSize}x{kernelSize})')
        axes[row, col].axis('off')

    plt.tight_layout()
    plt.show()