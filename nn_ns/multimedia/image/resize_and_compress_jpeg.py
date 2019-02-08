

'''
https://stackoverflow.com/questions/41718892/pillow-resizing-a-gif

from PIL import Image
image = Image.open("my_picture.jpg")
image = image.resize((image.size[0] // 2, image.size[1] // 2), Image.ANTIALIAS)  # decreases width and height of the image
image.save("out.jpg", optimize=True, quality=85)  # decreases its quality

'''

__all__ = '''
    save_jpeg
    resize_and_compress_jpeg
    '''.split()
from .resize_image__non_gif import resize_image__non_gif
# Pillow
from PIL import Image
from pathlib import Path

def save_jpeg(image, ofname_jpg, *, optimize:bool, quality:int):
    assert isinstance(image, Image.Image)
    assert quality >= 0

    path = Path(ofname_jpg)
    ext = path.suffix.lower()
    if ext not in ('jpg', 'jpeg'):
        raise ValueError('not jpeg path: {ofname_jpg!r}')
    image.save(ofname_jpg, optimize=optimize, quality=quality)

def resize_and_compress_jpeg(
    ifname_or_image, ofname, old_size2new_size_or_bound
    , *
    , is_new_size_bound:bool
    , optimize:bool
    , quality:int
    ):
    if ofname is not None: raise ValueError
    image = resize_image__non_gif(
                ifname_or_image, None, old_size2new_size_or_bound
                ,is_new_size_bound=bool(is_new_size_bound)
                )
    save_jpeg(image, ofname, optimize=optimize, quality=quality)
    return image


