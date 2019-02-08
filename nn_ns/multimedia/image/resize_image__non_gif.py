

'''
resize image

https://stackoverflow.com/questions/6444548/how-do-i-get-the-picture-size-with-pil
https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
https://stackoverflow.com/questions/41718892/pillow-resizing-a-gif

######## PIL - py2
######## Pillow - py3
########    download "Pillow" but package named by "PIL", too

[non-gif]
# According to Pillow 4.0x, the Image.resize function only works on a single image/frame.
#   not for ".gif"!!!!!!!!!

[.thumbnail vs .resize]
#   image.thumbnail(new_size_bound, Image.ANTIALIAS)
#       max_width, max_height = new_size_bound
#       keep the aspect ratio of old image
#   https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
#


'''

__all__ = '''
    resize_image__non_gif
    resize_image__non_gif__size
    resize_image__non_gif__bound
    '''.split()

from PIL import Image
import sys

def resize_image__non_gif__size(
    ifname_or_image, maybe_ofname, old_size2new_size_bound
    , *, method_kwargs=None
    ):
    return resize_image__non_gif__impl(
        ifname_or_image, maybe_ofname, old_size2new_size_bound
        ,maybe_method_kwargs=method_kwargs
        ,is_new_size_bound=False
        )
def resize_image__non_gif__bound(
    ifname_or_image, maybe_ofname, old_size2new_size_bound
    , *, method_kwargs=None
    ):
    return resize_image__non_gif__impl(
        ifname_or_image, maybe_ofname, old_size2new_size_bound
        ,maybe_method_kwargs=method_kwargs
        ,is_new_size_bound=True
        )
def resize_image__non_gif(
    ifname_or_image, maybe_ofname, old_size2new_size_or_bound
    , *, is_new_size_bound:bool, method_kwargs=None
    ):
    __method = 'thumbnail' if is_new_size_bound else 'resize'
    return resize_image__non_gif__impl(
        ifname_or_image, maybe_ofname, old_size2new_size_or_bound
        ,__method=__method
        ,maybe_method_kwargs=method_kwargs
        )


def resize_image__non_gif__impl(
    ifname_or_image
    ,maybe_ofname
    ,old_size2new_size_or_bound
    ,*
    ,__method
    ,maybe_method_kwargs
    ):
    '''
# allow: ifname == ofname
input:
    ifname_or_image :: Path | Image

    maybe_ofname :: None | Path

    old_size2new_size_or_bound
        :: (UInt, UInt) -> (UInt, UInt)
        :: (ImageSize -> ImageSize) | (ImageSize -> ImageSizeBound)
        size = (width, height)
        size_bound = (max_width, max_height)
        result is new_size or new_size_bound depended on __method

    __method :: String
        __method in ('resize', 'thumbnail')
    maybe_method_kwargs :: None | kwargs
        kwargs for __method
        e.g.
            for jpeg:
                optimize=True, quality=85
output:
    result_image :: Image
'''
    assert __method in ('resize', 'thumbnail')
    if maybe_method_kwargs is None:
        method_kwargs = {}
    else:
        method_kwargs = maybe_method_kwargs

    if isinstance(ifname_or_image, Image.Image):
        image = ifname_or_image
    else:
        ifname = ifname_or_image
        image = Image.open(ifname)

    width, height = image.size
    old_size = width, height

    #or: max_width, max_height
    new_width, new_height = old_size2new_size_or_bound(old_size)
    #or: new_size_bound
    new_size = new_width, new_height

    result_image = getattr(image, __method)(
        new_size, Image.ANTIALIAS, **method_kwargs)
    assert result_image is None
    result_image = image

    if maybe_ofname is not None:
        ofname = maybe_ofname
        result_image.save(ofname)
    return result_image




resize_image__non_gif__impl.__doc__
resize_image__non_gif.__doc__ = '''
__method = 'thumbnail' if is_new_size_bound else 'resize'
###### resize_image__non_gif__impl.__doc__:
    ''' + resize_image__non_gif__impl.__doc__
resize_image__non_gif__size.__doc__ = '''
__method = 'resize'
###### resize_image__non_gif__impl.__doc__:
    ''' + resize_image__non_gif__impl.__doc__
resize_image__non_gif__bound = '''
__method = 'thumbnail'
###### resize_image__non_gif__impl.__doc__:
    ''' + resize_image__non_gif__impl.__doc__



