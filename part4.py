import cv2
import numpy as np
import matplotlib.pyplot as plt

#function for reduce resolution
def reduceResolution(image, block_size):
    reducedImage = np.zeros_like(image)
    rows, cols = image.shape[:2]
    for i in range(0, rows, block_size):
        for j in range(0, cols, block_size):
            block = image[i:i+block_size, j:j+block_size]
            average_color = np.mean(block, axis=(0, 1))
            reducedImage[i:i+block_size, j:j+block_size] = average_color
    return reducedImage

imagePath = "/content/image.jpg"
image = cv2.imread(imagePath)

if image is None:
    print("Error: Unable to load image.")
else:
    reducedImage_3x3 = reduceResolution(image, 3)
    reducedImage_5x5 = reduceResolution(image, 5)
    reducedImage_7x7 = reduceResolution(image, 7)

    # Display
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))

    axes[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')

    axes[0, 1].imshow(cv2.cvtColor(reducedImage_3x3, cv2.COLOR_BGR2RGB))
    axes[0, 1].set_title('Resolution (3x3 blocks)')
    axes[0, 1].axis('off')

    axes[1, 0].imshow(cv2.cvtColor(reducedImage_5x5, cv2.COLOR_BGR2RGB))
    axes[1, 0].set_title('Resolution (5x5 blocks)')
    axes[1, 0].axis('off')

    axes[1, 1].imshow(cv2.cvtColor(reducedImage_7x7, cv2.COLOR_BGR2RGB))
    axes[1, 1].set_title('Resolution (7x7 blocks)')
    axes[1, 1].axis('off')

    plt.tight_layout()
    plt.show()
