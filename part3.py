import cv2
import numpy as np
import matplotlib.pyplot as plt


imagePath = "/content/image.jpg"
image = cv2.imread(imagePath)

if image is None:
    print("Error: Unable to load image.")
else:
    # Rotate by 45 degrees
    rows, cols = image.shape[:2]
    M45 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    rotated_45 = cv2.warpAffine(image, M45, (cols, rows))

    # Rotate by 90 degrees
    M90 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    rotated_90 = cv2.warpAffine(image, M90, (cols, rows))

    # Display results
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    axes[1].imshow(cv2.cvtColor(rotated_45, cv2.COLOR_BGR2RGB))
    axes[1].set_title('Rotated by 45 degrees')
    axes[1].axis('off')

    axes[2].imshow(cv2.cvtColor(rotated_90, cv2.COLOR_BGR2RGB))
    axes[2].set_title('Rotated by 90 degrees')
    axes[2].axis('off')

    plt.show()