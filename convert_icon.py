from PIL import Image
import os

def convert_to_ico():
    if os.path.exists('src/assets/icon.iconset/icon_256x256.png'):
        img = Image.open('src/assets/icon.iconset/icon_256x256.png')
        if not os.path.exists('src/assets/'):
            os.makedirs('src/assets/')
        img.save('src/assets/icon.ico', format='ICO')

if __name__ == '__main__':
    convert_to_ico()