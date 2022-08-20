import os
import random
import shutil



def grab_image():
    img_list = os.listdir('images')
    chosen_img = random.choice(img_list)

    os.replace(f'images/{chosen_img}', f'used_images/{chosen_img}')

    return chosen_img



