import cv2
import imageio
import os

# Folder with TIFF images
tif_folder = 'C:\\Users\\nsdev\\code\\biology\\p002\\data'
output_gif = 'output.gif'
tif_files = sorted([f for f in os.listdir(tif_folder) if f.lower().endswith('.png')])
frames = []
widths, heights = [], []

# min width and height
min_w, min_h = None, None
for tif in tif_files:
    img = cv2.imread(os.path.join(tif_folder, tif))
    h, w = img.shape[:2]
    if min_w is None or w < min_w:
        min_w = w
    if min_h is None or h < min_h:
        min_h = h

print(f'shape: {min_w}, {min_h}')
# Crop to min dimensions
for tif in tif_files:
    path = os.path.join(tif_folder, tif)
    img = cv2.imread(path)
    h, w = img.shape[:2]

    # Center crop
    top = (h - min_h) // 2
    left = (w - min_w) // 2
    cropped = img[top:top+min_h, left:left+min_w]

    img_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
    print(img_rgb.shape)
    frames.append(img_rgb)

# Save as GIF
imageio.mimsave(output_gif, frames, duration=2000, loop=0)


# with imageio.get_writer(output_gif, mode='I', duration=105.0, loop=0) as writer:
#     for tif in tif_files:
#         path = os.path.join(tif_folder, tif)
#         img = cv2.imread(path)

#         # Center crop to min_w x min_h
#         h, w = img.shape[:2]
#         top = (h - min_h) // 2
#         left = (w - min_w) // 2
#         cropped = img[top:top+min_h, left:left+min_w]

#         # BGR to RGB
#         rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)

#         writer.append_data(rgb)