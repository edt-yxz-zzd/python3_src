
image_path = r'E:\download\mz\fun\桃花庵歌1.png'
import imageio
image = imageio.imread(image_path)
print(image.size, image.shape)
import io
fout = io.BytesIO()
imageio.imsave(fout, image, format='png')
print(fout)
'''
# imageio.__init__
    from imageio.core.format import FormatManager
    formats = FormatManager()
# imageio.core.functions.get_reader/read
    format = formats.search_read_format(request)
    format = formats[format_name]
    reader = format.get_reader(request)
# imageio.core.imread
    image = reader.get_data(0)
'''
