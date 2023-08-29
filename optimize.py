import os
from PIL import Image, ImageOps

compress_size = 1.5
non_opt = './images/non_opt'
opt = './images/opt'

"""
    1. run -> pip3 install -r requirements.txt
    2. add 'Ok for posting?' company trip images into non_opt folder
    3. insert company trip name into folders
"""

folders = [
    
]


def make_folder_structure():
    try:
        os.makedirs('./images/non_opt')
    except FileExistsError:
        print("Non opt folder exists")
    try:
        os.makedirs('./images/opt')
    except FileExistsError:
        print('Opt folder exists')

    for folder in folders:
        try:
            if folder not in os.listdir(non_opt):
                try:
                    os.makedirs(f'{non_opt}/{folder}')
                except FileExistsError:
                    pass

            if folder not in os.listdir(opt):
                try:
                    os.makedirs(f'{opt}/{folder}')
                except FileExistsError:
                    pass
        except FileNotFoundError:
            print("Invalid folder structure")
    optimize_images()


def optimize_images():
    count = 0  # image count
    for i, folder in enumerate(os.listdir(non_opt)):
        print(folder)
        for j, file in enumerate(os.listdir(f'{non_opt}/{folders[i]}')):
            try:
                img = Image.open(f'{non_opt}/{folders[i]}/{file}')
                img = ImageOps.exif_transpose(img)
                compress = (int(img.size[0] / compress_size), int(img.size[1] / compress_size))
                print(f'{j}. original: {img.size} resampled: {compress} ')
                opt_img = img.resize(compress, resample=2)
                opt_img.save(f'{opt}/{folders[i]}/{j + 1} - {folder}.jpg', dpi=[300, 300])
                count += 1
            except KeyboardInterrupt:
                pass
    print(f'Total images from {len(folders)} folders: {count}')


if __name__ == '__main__':
    make_folder_structure()
