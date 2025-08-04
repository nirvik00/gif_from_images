import os
import imageio
from pylibCZIrw import czi as pyczi
import matplotlib.pyplot as plt
import cv2
import matplotlib.cm as cm

def read_gen_gif():
    #### input czi file path + name here like so
    input_czi_filename = "C:\\Users\\nsdev\\code\\biology\\p002\data\\newCZI_z=16_ch=3.czi" 
    #
    # files and gif animation stored here
    output_dir = "new_output2"

    try:
        os.mkdir(os.path.join(os.getcwd(), output_dir))
    except:
        pass # output_dir exists

    # image generation -> gif-animation and write to disk 
    with pyczi.open_czi(input_czi_filename) as czidoc:
        print(czidoc.total_bounding_box)
        z_num =czidoc.total_bounding_box['Z'][1]
        # generate image for each z-stack
        for i in range(z_num):
            img = czidoc.read(plane={'Z': i, 'C': 1})
            plt.imshow(img, cmap=cm.inferno, vmin=100, vmax=4000)
            plt.savefig(f'{output_dir}/img{i}.png')

        # make gif animation from images
        files = [f for f in os.listdir(output_dir) if f.lower().endswith('.png')]
        frames=[]
        for file in files:
            img = cv2.imread(os.path.join(output_dir,file))
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            frames.append(img_rgb)
        imageio.mimsave(f"{output_dir}/output.gif", frames, duration=1, loop=0)

read_gen_gif()