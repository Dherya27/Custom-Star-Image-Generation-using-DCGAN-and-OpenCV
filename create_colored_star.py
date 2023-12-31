# -*- coding: utf-8 -*-
"""create_colored_star.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wwbsrGx9SlPk_UF9qCh5YzLjOXJ9twML
"""

import cv2
import numpy as np
import os
import random
import math

# Define the path
output_directory = 'colored_stars_dataset'
os.makedirs(output_directory, exist_ok=True)

num_images = 100000
image_size = (64, 64)

for i in range(num_images):
    # Create a black background
    image = np.zeros((64, 64, 3), dtype=np.uint8)

    # Parameters for the star:
    num_points = 5
    outer_radius = np.random.randint(10, 23)
    inner_radius = outer_radius // 2
    start_angle = 0
    end_angle = 360

    center_x = np.random.randint(outer_radius, image_size[0] - outer_radius)
    center_y = np.random.randint(outer_radius, image_size[1] - outer_radius)

    color = (np.random.randint(256), np.random.randint(256), np.random.randint(256))

    # Draw the star on the image
    points = []
    for j in range(num_points * 2):
        angle = math.radians(start_angle + (j / (num_points * 2)) * (end_angle - start_angle))
        radius = outer_radius if j % 2 == 0 else inner_radius
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((int(x), int(y)))

    cv2.fillPoly(image, [np.array(points)], color)

    # Generate a random angle for rotation
    rotation_angle = np.random.uniform(0, 360)

    # Rotate the star
    M = cv2.getRotationMatrix2D((image_size[0] / 2, image_size[1] / 2), rotation_angle, 1)
    image = cv2.warpAffine(image, M, (image_size[0], image_size[1]))

    # Save
    filename = os.path.join(output_directory, f'star_image_{i}.png')
    cv2.imwrite(filename, image)

from google.colab import files

# Path
folder_path = 'colored_stars_dataset'
# Create zip file
!zip -r white_dataset.zip $folder_path

files.download('colored_dataset.zip')