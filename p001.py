import cv2
import imageio
import os

# Folder with TIFF images
tif_folder = 'path/to/tif/files'
output_gif = 'output.gif'

# Get all tif files, sorted
tif_files = sorted([f for f in os.listdir(tif_folder) if f.lower().endswith('.tif')])

# List to hold frames
frames = []

for tif in tif_files:
    path = os.path.join(tif_folder, tif)
    img = cv2.imread(path)  # OpenCV reads in BGR format
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB for imageio
    frames.append(img_rgb)

# Save as GIF (duration is per frame in seconds)
imageio.mimsave(output_gif, frames, duration=0.2)