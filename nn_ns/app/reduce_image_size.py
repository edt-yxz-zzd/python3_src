
r'''
e ../../python3_src/nn_ns/app/reduce_image_size.py
py -m nn_ns.app.reduce_image_size -i /sdcard/0my_files/p/IMG_20220428_170437.jpg -o /sdcard/0my_files/p/IMG_20220428_170437-quality-5.jpg  --quality 5
    bad
    96K
py -m nn_ns.app.reduce_image_size -i /sdcard/0my_files/p/IMG_20220428_170437.jpg -o /sdcard/0my_files/p/IMG_20220428_170437-quality-10.jpg  --quality 10
    not good
    135K
py -m nn_ns.app.reduce_image_size -i /sdcard/0my_files/p/IMG_20220428_170437.jpg -o /sdcard/0my_files/p/IMG_20220428_170437-quality-15.jpg  --quality 15
    ok
    182K
py -m nn_ns.app.reduce_image_size -i /sdcard/0my_files/p/IMG_20220428_170437.jpg -o /sdcard/0my_files/p/IMG_20220428_170437-quality-35.jpg  --quality 35
    451K
py -m nn_ns.app.reduce_image_size -i /sdcard/0my_files/p/IMG_20220428_170437.jpg -o /sdcard/0my_files/p/IMG_20220428_170437-quality-85.jpg  --quality 85
    1.9M
/sdcard/0my_files/p/IMG_20220428_170437.jpg
    4.4M
/sdcard/0my_files/p/IMG_20220428_170455.jpg
    6M
py -m nn_ns.app.reduce_image_size -i /sdcard/0my_files/p/IMG_20220428_170455.jpg -o /sdcard/0my_files/p/IMG_20220428_170455-quality-15.jpg  --quality 15
    312K

[[
https://roytuts.com/how-to-reduce-image-size-using-python/

import os, sys
from PIL import Image

orig_img_dir = "original_images/"
dirs = os.listdir(orig_img_dir)

print('Image Size Reduction Started...')

for img in dirs:
    if os.path.isfile(orig_img_dir + img):
        im = Image.open(orig_img_dir + img)
        img_name = os.path.basename(orig_img_dir + img)
        width, height = im.size
        im = im.resize((width, height), Image.ANTIALIAS)
        im.save('scaled_images/' + img_name)
        #im.save('optimized_images/' + img_name, optimize=True, quality=95)
        im.save('optimized_images/' + img_name, optimize=True, quality=85)

print('Image Size Reduction Done.')

The scaled_images folder contains the reduced images which are resized without passing optimize and quality parameters. The ANTIALIAS filter produces image with highest quality.

The optimized_images folder contains the reduced images which are resized with optimize and quality parameters. The optimize flag will do an extra pass on the image to find a way to reduce its size as much as possible. The default quality is 75, the quality value 85 will give you the optimized image with smaller size and quality of the image does not get affected much. The quality with 95 will produce image with much bigger size than quality with 85.
]]
#'''



from PIL import Image
from pathlib import Path

def reduce_image_size(ipath4img, opath4img, /, *, quality, exist_ok, may_width, may_height, may_scale):
    ipath4img = Path(ipath4img).resolve()
    opath4img = Path(opath4img).resolve()
    if not ipath4img.exists(): raise FileNotFoundError(ipath4img)
    if not exist_ok:
        if opath4img.exists(): raise FileExistsError(opath4img)

    im = Image.open(str(ipath4img))
    old_width, old_height = im.size
    if not may_scale is None:
        if not (may_width is None is may_height): raise TypeError
        scale = may_scale
        width = int(old_width * scale)
        height = int(old_height * scale)
    elif (may_width is None is may_height):
        width = old_width
        height = old_height
    else:
        if not may_width is None:
            width = may_width
        if not may_height is None:
            height = may_height

        if may_width is None:
            width = int(old_width * height / old_height)
        if may_height is None:
            height = int(old_height * width / old_width)
    (width, height)


    #scaled_im = im.resize((width, height), Image.ANTIALIAS)
        #DeprecationWarning: ANTIALIAS is deprecated and will be removed in Pillow 10 (2023-07-01). Use Resampling.LANCZOS instead.
        #
    scaled_im = im.resize((width, height), Image.Resampling.LANCZOS)
    scaled_im.save(opath4img, optimize=True, quality=quality)

def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='reduce_image_size'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, required=True
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, required=True
                        , help='output file path')
    parser.add_argument('--quality', type=int, required=True
                        , help='quality for jpeg #eg. 75')
    parser.add_argument('--scale', type=float
                        , default = None
                        , help='scale for width&height of output file')
    parser.add_argument('--width', type=int
                        , default = None
                        , help='width of output file')
    parser.add_argument('--height', type=int
                        , default = None
                        , help='height of output file')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    omode = 'wt' if args.force else 'xt'

    reduce_image_size(args.input, args.output, quality=args.quality, may_scale=args.scale, may_width=args.width, may_height=args.height, exist_ok=args.force)

if __name__ == "__main__":
    main()







